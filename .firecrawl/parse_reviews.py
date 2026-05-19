import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

def load_md(filepath):
    if filepath.endswith('.json'):
        with open(filepath, encoding='utf-8') as f:
            data = json.load(f)
        return data.get('markdown', '')
    else:
        with open(filepath, encoding='utf-8') as f:
            return f.read()

def parse_page(filepath):
    md = load_md(filepath)
    lines = md.split('\n')

    # Find 'All reviews' section
    start_idx = 0
    for i, l in enumerate(lines):
        if '## All reviews' in l:
            start_idx = i + 1
            break

    # Join continuation lines: line ending with \\ continues into next line
    # This handles [Name\\\nCOUNTRY•N review](url) split across lines
    joined = []
    i = start_idx
    while i < len(lines):
        l = lines[i]
        if l.rstrip().endswith('\\') and i + 1 < len(lines):
            combined = l.rstrip().rstrip('\\') + ' ' + lines[i+1].strip()
            joined.append(combined)
            i += 2
        else:
            joined.append(l)
            i += 1

    reviews = []
    i = 0
    while i < len(joined):
        line = joined[i].strip()

        # Reviewer line: [Name COUNTRY•N review](trustpilot.com/users/...)
        if 'trustpilot.com/users' in line and 'review' in line:
            # Pattern: [Name COUNTRY•N review(s)](url)  (after joining)
            m = re.search(
                r'\[([^\]]+?)\s+([A-Z]{2,3})\s*[•·]\s*(\d+)\s*reviews?\]\(https://www\.trustpilot\.com/users/',
                line
            )
            reviewer_name = m.group(1).strip() if m else None
            reviewer_country = m.group(2).strip() if m else None

            # Fallback: try splitting on bullet
            if not reviewer_name:
                m2 = re.search(r'\[(.+?)\s*[•·]\s*\d+\s*reviews?\]', line)
                if m2:
                    # Name + country both before bullet, country is last 2-letter token
                    chunk = m2.group(1)
                    parts = chunk.split()
                    if len(parts) >= 2 and re.match(r'^[A-Z]{2,3}$', parts[-1]):
                        reviewer_country = parts[-1]
                        reviewer_name = ' '.join(parts[:-1])
                    else:
                        reviewer_name = chunk

            review_date = None
            review_stars = None
            review_title = None
            review_url = None
            body_lines = []
            body_started = False
            tour_date = None  # "Experience date" shown separately

            j = i + 1
            while j < min(i + 35, len(joined)):
                l = joined[j].strip()

                # Standalone date (review posted date)
                date_m = re.match(r'^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d+,\s+\d{4}$', l)
                if date_m:
                    if not review_date:
                        review_date = l
                    elif not tour_date:
                        tour_date = l  # second date = experience date

                # Stars
                if review_stars is None:
                    sm = re.search(r'Rated (\d) out of 5', l)
                    if sm:
                        review_stars = int(sm.group(1))
                    elif 'stars-5.svg' in l and 'out of 5' in l:
                        review_stars = 5
                    elif 'stars-4.svg' in l and 'out of 5' in l:
                        review_stars = 4

                # Title + review URL
                if not review_title:
                    tm = re.match(
                        r'\[\*\*(.+?)\*\*\]\((https://www\.trustpilot\.com/reviews/[a-f0-9]+)\)', l
                    )
                    if tm:
                        review_title = tm.group(1)
                        review_url = tm.group(2)
                        body_started = True
                        j += 1
                        continue

                # Stop at next reviewer block
                if j > i + 2 and 'trustpilot.com/users' in l and 'review' in l:
                    break

                # Body text
                SKIP = {
                    'Unprompted review', 'Redirected', 'Company replied',
                    'Advertisement', 'Reply from Java Volcano Tour Operator', ''
                }
                if body_started and l and l not in SKIP:
                    if l.startswith('!') or l.startswith('#') or l.startswith('['):
                        j += 1
                        continue
                    skip_reply = any(x in l for x in [
                        'trustpilot.com', 'Dear ', 'Warm regards,',
                        'Java Volcano Tour Operator Team',
                        'Previous', 'Next page', 'How Trustpilot'
                    ])
                    # Skip JVTO reply lines (Thank you / We're) unless short enough to be body
                    is_reply_opener = (
                        l.startswith('Thank you') or l.startswith("We're") or
                        l.startswith('We are') or l.startswith("We've") or
                        l.startswith('Your ') or l.startswith('Hi ') or
                        l.startswith('Dear ')
                    )
                    if not skip_reply and not is_reply_opener and len(l) > 5:
                        body_lines.append(l)

                j += 1

            reviews.append({
                'reviewer': reviewer_name,
                'country': reviewer_country,
                'date': review_date,
                'experience_date': tour_date,
                'stars': review_stars,
                'title': review_title,
                'url': review_url,
                'body': ' '.join(body_lines) if body_lines else None,
            })

        i += 1

    return reviews


all_reviews = []
all_reviews += parse_page('.firecrawl/trustpilot-jvto-ss.json')
all_reviews += parse_page('.firecrawl/trustpilot-jvto-p2.json')
all_reviews += parse_page('.firecrawl/trustpilot-jvto-p3.json')

# Deduplicate by URL
seen_urls = set()
unique = []
for r in all_reviews:
    key = r['url'] or r['title']
    if key not in seen_urls:
        seen_urls.add(key)
        unique.append(r)

print(f'Total unique reviews: {len(unique)}')
print()
for r in unique:
    print('---')
    print(f"Name   : {r['reviewer']}  |  Country: {r['country']}  |  Stars: {r['stars']}")
    print(f"Date   : {r['date']}  |  Exp date: {r['experience_date']}")
    print(f"Title  : {r['title']}")
    print(f"URL    : {r['url']}")
    if r['body']:
        print(f"Body   : {r['body'][:400]}")

# Save as JSON for later use
import json as json2
with open('.firecrawl/reviews-structured.json', 'w', encoding='utf-8') as f:
    json2.dump(unique, f, ensure_ascii=False, indent=2)
print(f'\nSaved to .firecrawl/reviews-structured.json')
