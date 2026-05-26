# news — RSS Query Reference

## Topic Queries (Google News RSS)

| Topic | Query String |
|-------|--------------|
| Geopolitics | `geopolitics+may+2026` |
| AI Policy/Regulation | `AI+tech+policy+regulation+may+2026` |
| Science Breakthrough | `science+breakthrough+may+2026` |
| Economy/Trade/Tariffs | `economy+trade+tariff+may+2026` |
| AI Science/Math | `AI+science+math+breakthrough+2026` |

## RSS URL Template

```
https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US%3Aen
```

## Parsing RSS in Python

```python
import urllib.request, xml.etree.ElementTree as ET

def fetch_rss(query):
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US%3Aen"
    with urllib.request.urlopen(url) as resp:
        root = ET.parse(resp).getroot()
    items = []
    for item in root.findall(".//item"):
        items.append({
            "title": item.find("title").text.strip() if item.find("title") is not None else "",
            "link": item.find("link").text.strip() if item.find("link") is not None else "",
            "pubDate": item.find("pubDate").text.strip() if item.find("pubDate") is not None else "",
            "description": item.find("description").text.strip() if item.find("description") is not None else "",
        })
    return items
```

## Significance Criteria

Will this story matter in 6 months?
- [ ] Geopolitically significant (not just domestic noise)
- [ ] Connects to existing wiki threads
- [ ] Has lasting implications vs. is a 1-day cycle story
- [ ] Substantive enough to write 2-3 paragraphs of context