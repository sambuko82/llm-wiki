"""Focused tests for scripts/verify_output_index.py (the output/INDEX.md guard).

These exercise the pure core (no git/disk needed): the five required scenarios
plus parser robustness against URL slugs, superseded-by columns, and prose.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.verify_output_index import find_problems, parse_indexed_paths

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"


def _problems(indexed, existing, tracked_md, excludes=None):
    return find_problems(list(indexed), set(existing), set(tracked_md), list(excludes or []))


def test_clean_valid_index_has_no_problems():
    assert _problems(["website/a.md"], {"website/a.md"}, {"website/a.md"}) == []


def test_stale_indexed_path_fails():
    problems = _problems(["website/gone.md"], existing=set(), tracked_md=set())
    assert any("[stale]" in p and "website/gone.md" in p for p in problems)


def test_renamed_path_still_referenced_fails():
    # File renamed old -> new: the old path is still in the index (stale) and the
    # new file is not yet indexed (uncovered).
    problems = _problems(
        ["website/old-name.md"],
        existing={"website/new-name.md"},
        tracked_md={"website/new-name.md"},
    )
    assert any("[stale]" in p and "website/old-name.md" in p for p in problems)
    assert any("[uncovered]" in p and "website/new-name.md" in p for p in problems)


def test_new_output_file_missing_from_index_fails():
    problems = _problems([], existing={"website/new.md"}, tracked_md={"website/new.md"})
    assert any("[uncovered]" in p and "website/new.md" in p for p in problems)


def test_duplicate_index_entry_fails():
    problems = _problems(
        ["website/a.md", "website/a.md"],
        existing={"website/a.md"},
        tracked_md={"website/a.md"},
    )
    assert any("[duplicate]" in p and "website/a.md" in p for p in problems)


def test_explicitly_excluded_markdown_is_not_required():
    problems = _problems(
        [],
        existing={"website/schema/x.receipt.md"},
        tracked_md={"website/schema/x.receipt.md"},
        excludes=["website/schema/*.receipt.md"],
    )
    assert problems == []


def test_parser_reads_only_table_column1_filepaths():
    text = (
        "| File | URL |\n"
        "|---|---|\n"
        "| `website/pages/homepage.md` | `/` |\n"
        "| `_archive/old.md` | `website/pages/homepage.md` |\n"  # col2 'superseded-by' ignored
        "| ~~`faq/papuma.md` resolved~~ | done |\n"             # struck-through note ignored
        "Verification receipt: `website/schema/x.receipt.md`\n"  # prose (non-table) ignored
    )
    assert parse_indexed_paths(text) == ["website/pages/homepage.md", "_archive/old.md"]


def _git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True)


def test_commit_hook_validates_staged_tree_not_worktree():
    """A staged new file with the INDEX fix left only in the worktree must still block."""
    index_one = "# Output Index\n\n| File | URL |\n|---|---|\n| `website/a.md` | `/a` |\n"
    index_two = index_one + "| `website/b.md` | `/b` |\n"
    commit_payload = '{"tool_name":"Bash","tool_input":{"command":"git commit -m x"}}'

    with tempfile.TemporaryDirectory() as temp:
        repo = Path(temp)
        (repo / "scripts").mkdir()
        shutil.copy(SCRIPTS_DIR / "verify_output_index.py", repo / "scripts" / "verify_output_index.py")
        shutil.copy(SCRIPTS_DIR / "output_index_exclude.txt", repo / "scripts" / "output_index_exclude.txt")
        (repo / "output" / "website").mkdir(parents=True)
        (repo / "output" / "website" / "a.md").write_text("a", encoding="utf-8")
        (repo / "output" / "INDEX.md").write_text(index_one, encoding="utf-8")
        _git(repo, "init", "-q")
        _git(repo, "config", "user.email", "t@example.com")
        _git(repo, "config", "user.name", "t")
        _git(repo, "add", "-A")
        _git(repo, "commit", "-q", "-m", "init")

        # Stage a NEW output file; fix INDEX.md only in the worktree (forgot `git add`).
        (repo / "output" / "website" / "b.md").write_text("b", encoding="utf-8")
        _git(repo, "add", "output/website/b.md")
        (repo / "output" / "INDEX.md").write_text(index_two, encoding="utf-8")

        env = {**os.environ, "CLAUDE_PROJECT_DIR": str(repo)}
        blocked = subprocess.run(
            [sys.executable, "scripts/verify_output_index.py", "--hook"],
            cwd=repo, env=env, input=commit_payload, capture_output=True, text=True,
        )
        assert blocked.returncode == 2, blocked.stderr + blocked.stdout
        assert "website/b.md" in blocked.stderr

        # Stage the INDEX fix too -> staged tree is consistent -> allow.
        _git(repo, "add", "output/INDEX.md")
        allowed = subprocess.run(
            [sys.executable, "scripts/verify_output_index.py", "--hook"],
            cwd=repo, env=env, input=commit_payload, capture_output=True, text=True,
        )
        assert allowed.returncode == 0, allowed.stderr + allowed.stdout
