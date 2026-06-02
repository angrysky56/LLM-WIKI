import httpx, xml.etree.ElementTree as ET, urllib3, json, sys
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

results = {}
for name, url in feeds.items():
    try:
        r = client.get(url)
        root = ET.fromstring(r.text)
        items = []
        for item in root.findall('.//item')[:18]:
            t = item.findtext('title') or ''
            l = item.findtext('link') or ''
            p = item.findtext('pubDate') or ''
            d = item.findtext('description') or ''
            items.append({'title': t, 'link': l, 'pubDate': p, 'desc': d[:300]})
        results[name] = {'ok': True, 'count': len(items), 'items': items}
    except Exception as e:
        results[name] = {'ok': False, 'error': str(e)}

print(json.dumps(results, indent=2, default=str))
