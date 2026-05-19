import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('.firecrawl/reviews-structured.json', encoding='utf-8') as f:
    reviews = json.load(f)

# Crew name normalization map (raw mention -> canonical)
CREW_GUIDE = {
    'fauzi': 'Fauzi', 'faozi': 'Fauzi',
    'kiki': 'Kiki',
    'anjas': 'Anjas',
    'rendi': 'Rendi',
    'gufron': 'Gufron',
    'taufik': 'Taufik', 'toufic': 'Taufik', 'toufiic': 'Taufik',
    'ahboy': 'Ahboy', 'eboy': 'Ahboy', 'ehboy': 'Ahboy', 'oboy': 'Ahboy',
    'aboy': 'Ahboy', 'boy': 'Boy/Ahboy',
    'boi': 'Boy/Ahboy',
    'sulis': 'Sulis',
    'fredy': 'Fredy', 'freddy': 'Fredy',
}
CREW_DRIVER = {
    'yandi': 'Yandi',
    'holili': 'Holili',
    'joyo': 'Joyo', 'joy': 'Joyo', 'goyo': 'Joyo',
    'dika': 'Dika',
    'johan': 'Johan',
    'nur': 'Nur',
    'fredi': 'Fredi (driver)', 'fredy': 'Fredy',
}

COUNTRY_NAMES = {
    'ID': 'Indonesia', 'SG': 'Singapore', 'MY': 'Malaysia', 'AU': 'Australia',
    'GB': 'UK', 'US': 'USA', 'DE': 'Germany', 'HK': 'Hong Kong', 'TH': 'Thailand',
    'PL': 'Poland', 'IN': 'India', 'FR': 'France', 'NL': 'Netherlands',
}

def extract_crew(text):
    if not text:
        return [], []
    text_lower = text.lower()
    guides = []
    drivers = []
    for k, v in CREW_GUIDE.items():
        if k in text_lower and v not in guides:
            guides.append(v)
    for k, v in CREW_DRIVER.items():
        if k in text_lower:
            # Avoid double-counting Fredy/Fredi
            if v == 'Fredy' and 'Fredy (driver)' in drivers:
                continue
            if v not in drivers:
                drivers.append(v)
    return sorted(set(guides)), sorted(set(drivers))

def infer_package(r):
    text = ((r.get('title') or '') + ' ' + (r.get('body') or '')).lower()
    title_raw = (r.get('title') or '').lower()

    if 'ultimate volcano journey' in text or ('bali' in text and 'ijen' in text and 'bromo' in text and 'madakaripura' in text):
        return 'Ultimate Volcano Journey 3D2N Bali→Ijen→Bromo→Madakaripura→SUB'
    if '4d3n' in text and 'papuma' in text:
        return '4D3N SUB: Ijen-Papuma-Tumpak Sewu-Bromo'
    if '4d3n' in text and 'tumpak sewu' in text and 'bromo' in text and 'ijen' in text:
        return '4D3N SUB: Ijen-Tumpak Sewu-Bromo'
    if '4d3n' in text and 'bali' in text and 'surabaya' in text:
        return '4D3N Bali→SUB'
    if '4d2n' in text and ('bali' in text or 'surabaya' in text):
        return '4D2N Bali→SUB'
    if '3d2n' in text and 'ijen' in text and 'bromo' in text and ('madakaripura' in text or 'madakapuri' in text):
        return '3D2N: Ijen-Bromo-Madakaripura'
    if '3d2n' in text and 'bromo' in text and 'ijen' in text:
        return '3D2N: Bromo-Ijen'
    if '3d2n' in text and ('tumpak sewu' in text or 'bromo' in text):
        return '3D2N: Bromo-Tumpak Sewu'
    if 'kawah ijen' in text or ('ijen' in text and 'bromo' not in text):
        return 'Ijen Day/Night Tour'
    if 'bromo' in text and 'ijen' in text and 'tumpak sewu' in text:
        return '4D3N SUB: Ijen-Tumpak Sewu-Bromo'
    if 'bromo' in text and 'ijen' in text:
        return '3D2N: Bromo-Ijen'
    if 'bromo' in text and 'tumpak sewu' in text:
        return '3D2N: Bromo-Tumpak Sewu'
    if 'surabaya' in text and 'bali' in text:
        return 'SUB-Bali Transfer Tour'
    return 'Unknown'

def flag(country):
    flags = {
        'ID': '🇮🇩', 'SG': '🇸🇬', 'MY': '🇲🇾', 'AU': '🇦🇺', 'GB': '🇬🇧',
        'US': '🇺🇸', 'DE': '🇩🇪', 'HK': '🇭🇰', 'TH': '🇹🇭', 'PL': '🇵🇱',
        'IN': '🇮🇳', 'FR': '🇫🇷', 'NL': '🇳🇱',
    }
    return flags.get(country, '🌐')

lines = []
lines.append('---')
lines.append('type: reviews')
lines.append('title: Trustpilot Reviews — Full Structured Catalog')
lines.append('last_updated: 2026-05-18')
lines.append('sources: [trustpilot-scrape-2026-05-18]')
lines.append('platform: Trustpilot')
lines.append('rating: 4.8')
lines.append('review_count: 51')
lines.append('last_verified: 2026-05-18')
lines.append('---')
lines.append('')
lines.append('# Trustpilot Reviews — Full Structured Catalog')
lines.append('')
lines.append('Live scrape: 2026-05-18. 49 reviews with full text captured (2 platform-side without text body).')
lines.append('Source: [[reviews/trustpilot-compilation]] | Raw data: `.firecrawl/reviews-structured.json`')
lines.append('')
lines.append('## Summary Table')
lines.append('')
lines.append('| # | Date | Name | Country | ⭐ | Package | Guides | Drivers | Title |')
lines.append('|---|---|---|---|---|---|---|---|---|')

for idx, r in enumerate(reviews, 1):
    name = r['reviewer'] or '—'
    country = r['country'] or '?'
    country_display = f"{flag(country)} {COUNTRY_NAMES.get(country, country)}"
    stars = '★' * (r['stars'] or 0)
    date = r['date'] or '—'
    title = (r['title'] or '—')[:60]
    guides, drivers = extract_crew(r['body'])
    package = infer_package(r)
    lines.append(
        f"| {idx} | {date} | {name} | {country_display} | {stars} | {package} | {', '.join(guides) or '—'} | {', '.join(drivers) or '—'} | [{title}]({r['url'] or '#'}) |"
    )

lines.append('')
lines.append('## Full Review Entries')
lines.append('')
lines.append('Format: metadata block → verbatim review text → crew & package tags.')
lines.append('')

for idx, r in enumerate(reviews, 1):
    name = r['reviewer'] or 'Anonymous'
    country = r['country'] or '?'
    country_name = COUNTRY_NAMES.get(country, country)
    date = r['date'] or '—'
    exp_date = r['experience_date'] or '—'
    stars = '★' * (r['stars'] or 0) + '☆' * (5 - (r['stars'] or 0))
    title = r['title'] or '(no title)'
    url = r['url'] or ''
    body = r['body'] or '*(no text)*'
    guides, drivers = extract_crew(r['body'])
    package = infer_package(r)

    # Clean body: remove reply text (dates, JVTO boilerplate)
    # Remove trailing date artifacts and reply snippets
    body_clean = re.sub(r'\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d+,\s+\d{4}.*', '', body, flags=re.DOTALL)
    body_clean = body_clean.strip()
    # Remove common JVTO reply openers that leaked into body
    for pattern in [
        r"We're so glad.*", r"We're delighted.*", r"We're thrilled.*",
        r"We are delighted.*", r'Java Volcano Tour Operator.*',
        r'Hope to see you again.*', r'Hope to welcome.*',
        r'Rendi and.*will be.*', r"We'd be.*",
    ]:
        body_clean = re.sub(pattern, '', body_clean, flags=re.DOTALL | re.IGNORECASE).strip()

    lines.append(f'### {idx}. {name} — {title}')
    lines.append('')
    lines.append(f'| Field | Value |')
    lines.append(f'|---|---|')
    lines.append(f'| **Reviewer** | {name} |')
    lines.append(f'| **Country** | {flag(country)} {country_name} |')
    lines.append(f'| **Posted** | {date} |')
    lines.append(f'| **Experience date** | {exp_date} |')
    lines.append(f'| **Stars** | {stars} ({r["stars"]}/5) |')
    lines.append(f'| **Package (inferred)** | {package} |')
    lines.append(f'| **Guides mentioned** | {", ".join(guides) if guides else "—"} |')
    lines.append(f'| **Drivers mentioned** | {", ".join(drivers) if drivers else "—"} |')
    lines.append(f'| **Review URL** | {url} |')
    lines.append('')
    lines.append('> ' + body_clean.replace('\n', '  \n> '))
    lines.append('')

lines.append('---')
lines.append('')
lines.append('-> [[reviews/trustpilot-compilation]] | -> [[people/crew-registry]] | -> [[products/packages-overview]]')

output = '\n'.join(lines)
out_path = 'wiki/reviews/trustpilot-all-reviews.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Written: {out_path}')
print(f'Reviews: {len(reviews)}')
