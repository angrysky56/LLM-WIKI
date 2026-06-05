#!/usr/bin/env python3
"""RSS discovery for news-agent — June 5, 2026"""
import httpx, xml.etree.ElementTree as ET, urllib3, json, sys
urllib3.disable_warnings()
client = httpx.Client(timeout=15.0, verify=False, follow_redirects=True)

feeds = {
    'BBC World': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'Al Jazeera': 'https://www.aljazeera.com/xml/rss/all.xml',
    'NYT World': 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'Guardian': 'https://www.theguardian.com/world/rss',
    'Bloomberg': 'https://feeds.bloomberg.com/markets/news.rss',
}

# Also search Google News RSS for specific carryover topics
google_feeds = {
    # Follow-ups from carryover
    'GN-US House Iran war powers': 'https://news.google.com/rss/search?q=US+House+war+powers+Iran+Trump+senate+vote&hl=en-US&gl=US&ceid=US:en',
    'GN-Israel Lebanon ceasefire': 'https://news.google.com/rss/search?q=Israel+Lebanon+Hezbollah+ceasefire+June+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Kim nuclear expansion': 'https://news.google.com/rss/search?q=Kim+Jong+Un+nuclear+exponential+arsenal+June+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Somalia Mogadishu': 'https://news.google.com/rss/search?q=Somalia+Mogadishu+fighting+June+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Ebola DRC Kenya': 'https://news.google.com/rss/search?q=Ebola+DRC+Uganda+Kenya+June+2026&hl=en-US&gl=US&ceid=US:en',
    # Russia-Ukraine
    'GN-Russia Ukraine': 'https://news.google.com/rss/search?q=Russia+Ukraine+war+June+2026&hl=en-US&gl=US&ceid=US:en',
    # Colombia runoff
    'GN-Colombia Espriella': 'https://news.google.com/rss/search?q=Colombia+Espriella+runoff+Trump+June+2026&hl=en-US&gl=US&ceid=US:en',
    # SpaceX IPO
    'GN-SpaceX IPO': 'https://news.google.com/rss/search?q=SpaceX+IPO+trading+June+2026&hl=en-US&gl=US&ceid=US:en',
    # Anthropic IPO
    'GN-Anthropic IPO': 'https://news.google.com/rss/search?q=Anthropic+IPO+pricing+June+2026&hl=en-US&gl=US&ceid=US:en',
    # AI policy / breakthrough
    'GN-AI breakthrough': 'https://news.google.com/rss/search?q=AI+breakthrough+June+2026&hl=en-US&gl=US&ceid=US:en',
    # Fresh topics — geopolitics, science
    'GN-Geopolitics conflict': 'https://news.google.com/rss/search?q=geopolitics+conflict+June+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Science health': 'https://news.google.com/rss/search?q=science+breakthrough+June+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-China Taiwan': 'https://news.google.com/rss/search?q=China+Taiwan+June+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Trade tariffs': 'https://news.google.com/rss/search?q=trade+tariffs+US+China+June+2026&hl=en-US&gl=US&ceid=US:en',
    # US-Canada 51st state / USMCA
    'GN-US Canada trade': 'https://news.google.com/rss/search?q=US+Canada+trade+51st+state+June+2026&hl=en-US&gl=US&ceid=US:en',
}

results = {}
for name, url in {**feeds, **google_feeds}.items():
    try:
        r = client.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'})
        if r.status_code != 200:
            results[name] = {'status': r.status_code, 'items': []}
            continue
        root = ET.fromstring(r.text)
        items = []
        for item in root.findall('.//item')[:12]:
            items.append({
                'title': item.findtext('title', ''),
                'link': item.findtext('link', ''),
                'pubDate': item.findtext('pubDate', ''),
                'description': (item.findtext('description', '') or '')[:300]
            })
        results[name] = {'status': r.status_code, 'items': items}
    except Exception as e:
        results[name] = {'status': 'error', 'error': str(e), 'items': []}

# Write to file
outpath = '/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_output.json'
with open(outpath, 'w') as f:
    json.dump(results, f, indent=2)
print(f'Done. {len(results)} feeds fetched.')
print(f'Output: {outpath}')