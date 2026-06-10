import httpx
import xml.etree.ElementTree as ET
import json

client = httpx.Client(timeout=15.0, verify=False, follow_redirects=True)

standard_feeds = {
    'BBC World': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'Al Jazeera': 'https://www.aljazeera.com/xml/rss/all.xml',
    'NYT World': 'https://rss.nytimes.com/services/xml/rss/nyt/World.xml',
    'Guardian': 'https://www.theguardian.com/world/rss',
    'Bloomberg': 'https://feeds.bloomberg.com/markets/news.rss',
}

results = {}
for name, url in standard_feeds.items():
    try:
        r = client.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        results[name] = {'status': r.status_code, 'items': []}
        if r.status_code == 200:
            root = ET.fromstring(r.text)
            count = 0
            for item in root.findall('.//item'):
                title = item.findtext('title', '')
                pubdate = item.findtext('pubDate', '')
                desc = item.findtext('description', '')
                link = item.findtext('link', '')
                results[name]['items'].append({
                    'title': title.strip(),
                    'pubdate': pubdate.strip(),
                    'desc': desc.strip()[:200],
                    'link': link.strip()
                })
                count += 1
                if count >= 12:
                    break
    except Exception as e:
        results[name] = {'status': 'error', 'error': str(e), 'items': []}

with open('/tmp/rss_standard.json', 'w') as f:
    json.dump(results, f, indent=2)

for name, data in results.items():
    status = data['status']
    n = len(data['items'])
    print(f"{name}: {status} ({n} items)")
    for item in data['items'][:3]:
        print(f"  - {item['title'][:100]}")
    print()