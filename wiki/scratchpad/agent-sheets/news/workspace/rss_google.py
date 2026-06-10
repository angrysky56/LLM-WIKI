import httpx
import xml.etree.ElementTree as ET
import json

client = httpx.Client(timeout=15.0, verify=False, follow_redirects=True)

# Google News RSS queries built from carryover Open items + fixed gaps
google_queries = {
    'GN-Ceasefire-Tyre': 'https://news.google.com/rss/search?q=israel+tyre+lebanon+ceasefire&hl=en-US&gl=US&ceid=US:en',
    'GN-Iran-tensions': 'https://news.google.com/rss/search?q=us+iran+tensions+ceasefire+talks+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Peru-election': 'https://news.google.com/rss/search?q=peru+presidential+runoff+election+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Venezuela-protests': 'https://news.google.com/rss/search?q=venezuela+protests+2026+Maduro&hl=en-US&gl=US&ceid=US:en',
    'GN-Chornobyl': 'https://news.google.com/rss/search?q=chornobyl+nuclear+restart+IAEA+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Russia-peace': 'https://news.google.com/rss/search?q=russia+ukraine+peace+conditions+europe+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-AI-IPO': 'https://news.google.com/rss/search?q=ai+IPO+pipeline+OpenAI+Anthropic+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-USMCA': 'https://news.google.com/rss/search?q=USMCA+tariff+review+deadline+Mexico+Canada&hl=en-US&gl=US&ceid=US:en',
    'GN-Armenia-Russia': 'https://news.google.com/rss/search?q=armenia+pashinyan+russia+response+election&hl=en-US&gl=US&ceid=US:en',
    'GN-World-Cup': 'https://news.google.com/rss/search?q=2026+world+cup+usa+security+visa+disputes&hl=en-US&gl=US&ceid=US:en',
    'GN-Fed-rates': 'https://news.google.com/rss/search?q=federal+reserve+interest+rate+hike+CPI+June+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Ukraine-drones': 'https://news.google.com/rss/search?q=ukraine+drone+strikes+russia+missile+plant&hl=en-US&gl=US&ceid=US:en',
    'GN-South-Africa-xenophobia': 'https://news.google.com/rss/search?q=south+africa+xenophobia+attacks+immigrants+2026&hl=en-US&gl=US&ceid=US:en',
    'GN-Belfast-riots': 'https://news.google.com/rss/search?q=belfast+northern+ireland+riots+immigration+stabbing&hl=en-US&gl=US&ceid=US:en',
}

results = {}
for name, url in google_queries.items():
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
                if count >= 5:
                    break
    except Exception as e:
        results[name] = {'status': 'error', 'error': str(e), 'items': []}

with open('/tmp/rss_google.json', 'w') as f:
    json.dump(results, f, indent=2)

for name, data in results.items():
    status = data['status']
    n = len(data['items'])
    print(f"{name}: {status} ({n} items)")
    for item in data['items'][:3]:
        print(f"  - {item['title'][:120]}")
    print()