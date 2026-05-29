import urllib.request, urllib.parse, xml.etree.ElementTree as ET

def fetch_arxiv_ids(ids):
    id_list = ','.join(ids)
    url = f'https://export.arxiv.org/api/query?id_list={id_list}&max_results=10'
    with urllib.request.urlopen(url, timeout=30) as resp:
        root = ET.parse(resp).getroot()
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    results = []
    for entry in root.findall('a:entry', ns):
        results.append({
            'id': entry.find('a:id', ns).text.strip().split('/abs/')[-1],
            'title': entry.find('a:title', ns).text.strip().replace('\n', ' '),
            'authors': [a.find('a:name', ns).text for a in entry.findall('a:author', ns)][:3],
            'summary': entry.find('a:summary', ns).text.strip(),
            'categories': [c.get('term') for c in entry.findall('a:category', ns)][:3],
            'published': entry.find('a:published', ns).text[:10],
        })
    return results

candidates = ['2605.30343', '2605.30329', '2605.30335', '2605.30322', '2605.30327', '2605.30353', '2605.30314']
papers = fetch_arxiv_ids(candidates)

for p in papers:
    print(f'=== {p["id"]} ===')
    print(f'Title: {p["title"][:90]}')
    print(f'Authors: {p["authors"]}')
    print(f'Summary: {p["summary"][:400]}')
    print()