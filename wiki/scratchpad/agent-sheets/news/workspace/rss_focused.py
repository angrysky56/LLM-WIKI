import httpx, xml.etree.ElementTree as ET, urllib3, json
urllib3.disable_warnings()
client = httpx.Client(timeout=20.0, verify=False, follow_redirects=True,
                       headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'})

# Google News focused queries for stories we need more detail on
queries = {
    'Israel Hezbollah ceasefire': 'Israel+Hezbollah+ceasefire+Trump+de-escalation',
    'Iran US peace deal': 'Iran+US+peace+deal+Hormuz+June+2026',
    'Anthropic share offering trillion': 'Anthropic+valuation+share+sale+2026',
    'Ebola Kenya court ruling': 'Ebola+Kenya+court+ruling+quarantine',
    'Russia Kyiv strikes June 2': 'Russia+Kyiv+strikes+June+2+2026',
    'Trump Brazil tariff 25': 'Trump+Brazil+25+tariff',
    'Lebanon ceasefire partial': 'Israel+Lebanon+ceasefire+Beirut',
    'Russia Ukraine weakness strikes': 'Russia+Ukraine+strikes+rubble',
}

results = {}
for name, q in queries.items():
    try:
        url = f'https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en'
        r = client.get(url)
        root = ET.fromstring(r.text)
        items = []
        for item in root.findall('.//item')[:8]:
            t = item.findtext('title') or ''
            l = item.findtext('link') or ''
            p = item.findtext('pubDate') or ''
            d = item.findtext('description') or ''
            items.append({'title': t, 'pubDate': p, 'desc': d[:300], 'link': l})
        results[name] = items
    except Exception as e:
        results[name] = {'error': str(e)}

print(json.dumps(results, indent=2, default=str))
