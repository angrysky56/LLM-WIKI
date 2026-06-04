#!/usr/bin/env python3
"""RSS discovery for 2026-06-04 news cycle.
Per news-agent SKILL: use httpx + xml.etree.ElementTree in terminal.
Returns top N titles per feed for the past ~48 hours.
"""
import httpx, xml.etree.ElementTree as ET, urllib3, json, re
from datetime import datetime, timezone, timedelta
urllib3.disable_warnings()

client = httpx.Client(timeout=20.0, verify=False, follow_redirects=True,
                      headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'})

feeds = {
    'BBC World': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'Al Jazeera': 'https://www.aljazeera.com/xml/rss/all.xml',
    'NYT World': 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'Guardian': 'https://www.theguardian.com/world/rss',
    'Bloomberg': 'https://feeds.bloomberg.com/markets/news.rss',
}

# Cutoff: stories from past 36 hours (focus on today)
now = datetime.now(timezone.utc)
cutoff = now - timedelta(hours=36)

results = {}
for name, url in feeds.items():
    try:
        r = client.get(url)
        if r.status_code != 200:
            results[name] = {'status': r.status_code, 'stories': []}
            continue
        root = ET.fromstring(r.text)
        stories = []
        for item in root.findall('.//item')[:20]:
            title = (item.findtext('title') or '').strip()
            desc = (item.findtext('description') or '').strip()
            link = (item.findtext('link') or '').strip()
            pub = (item.findtext('pubDate') or '').strip()
            # try to parse
            try:
                # RFC 822 like "Wed, 04 Jun 2026 05:30:00 GMT"
                from email.utils import parsedate_to_datetime
                pub_dt = parsedate_to_datetime(pub)
                if pub_dt.tzinfo is None:
                    pub_dt = pub_dt.replace(tzinfo=timezone.utc)
            except Exception:
                pub_dt = None
            stories.append({
                'title': title,
                'link': link,
                'pubDate': pub,
                'pub_dt': pub_dt.isoformat() if pub_dt else None,
                'description': re.sub(r'<[^>]+>', '', desc)[:400],
            })
        results[name] = {'status': 200, 'stories': stories}
    except Exception as e:
        results[name] = {'status': 'error', 'error': str(e), 'stories': []}

# Print compact summary: top 12 per feed
print('=' * 80)
print(f'RSS DISCOVERY — {now.isoformat()}')
print('=' * 80)
for name, info in results.items():
    print(f'\n--- {name} (status: {info.get("status")}) ---')
    for s in info['stories'][:12]:
        pub_short = s['pubDate'][:25] if s['pubDate'] else '????'
        print(f'  [{pub_short}] {s["title"][:120]}')
print()
print('=' * 80)
print('STORY DATA (full):')
print('=' * 80)
print(json.dumps({k: {'status': v.get('status'), 'count': len(v.get('stories', []))} for k, v in results.items()}, indent=2))

# Save full data for later inspection
with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_2026-06-04.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)
print('\nFull data saved to workspace/rss_2026-06-04.json')
