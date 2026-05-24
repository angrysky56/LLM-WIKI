# News Source URL Patterns & Fetch Failure Modes

## RSS Discovery (Primary Method)

Use Google News RSS as the primary discovery mechanism. Topic queries that return structured results reliably:

```bash
curl -s "https://news.google.com/rss/search?q=geopolitics+may+2026&hl=en-US&gl=US&ceid=US%3Aen"
curl -s "https://news.google.com/rss/search?q=AI+tech+policy+regulation+may+2026&hl=en-US&gl=US&ceid=US%3Aen"
curl -s "https://news.google.com/rss/search?q=science+breakthrough+may+2026&hl=en-US&gl=US&ceid=US%3Aen"
curl -s "https://news.google.com/rss/search?q=economy+trade+tariff+may+2026&hl=en-US&gl=US&ceid=US%3Aen"
curl -s "https://news.google.com/rss/search?q=Ebola+outbreak+DRC+may+2026&hl=en-US&gl=US&ceid=US%3Aen"
curl -s "https://news.google.com/rss/search?q=SpaceX+IPO+Starship+may+2026&hl=en-US&gl=US&ceid=US%3Aen"
```

RSS returns XML with `<title>`, `<link>`, `<pubDate>` for each `<item>`. Many items = active story; empty = no recent coverage. When RSS returns empty for a known carryover story, use Google News search directly for that story.

---

## BBC

**Pattern:** `https://www.bbc.com/news/articles/{article-id}` where `article-id` is a alphanumeric string like `c0l3z93nwgdo`

**Failure mode:** defuddle consistently returns 404 on BBC article ID URLs, even when the article exists. The article-id format changed and defuddle cannot resolve the redirects.

**Working approach:**
1. Visit `https://www.bbc.com/news/world` with browser
2. Extract the article link href from the rendered page (clickable elements have ref IDs)
3. Feed the full article URL (as seen in browser) to `wiki_fetch_url`

**Alternative when browser fails:** Use Google News search with the article title, extract the canonical BBC link from results, use that with `wiki_fetch_url`.

---

## Al Jazeera

**Pattern:** `https://www.aljazeera.com/news/YYYY/M/D/{slug}` — date-based subdirectory, slug is lowercase with hyphens.

**Working approach:** The date-based pattern works when slug matches. Direct article URL from browser section page is most reliable.

**Failure mode:** defuddle returns 404 when slug format changes. Use browser to get current working URL.

---

## Reuters

**Pattern:** `https://www.reuters.com/{world|world/{region}}/...` — title in path.

**Failure mode:** Reuters has aggressive bot detection (DataDome device check blocks browser). defuddle also frequently fails with 404 or 500.

**Working approach:** Use Google News search to get Reuters canonical URL from results. Do NOT attempt direct Reuters URL via browser or defuddle — both will fail or get blocked.

---

## Google News as URL Resolver (Universal Pattern)

When direct publisher URLs fail, use Google News as a canonical URL aggregator:

```
1. Navigate to: https://news.google.com/search?q={story+keywords}&hl=en-US&gl=US&ceid=US%3Aen
2. Read the Google News result snippet — it contains the canonical publisher link
3. Use that exact URL (not the Google redirect) with wiki_fetch_url
```

This works because Google News indexes the actual publisher canonical URLs, not redirects.

**Query construction:** Use `+` for multi-word phrases, quotes for exact matches, `when:1d` or `when:1w` for recent only.

---

## Quick Reference: Which Method to Use

| Source | Browser section page | Google News search | Direct URL | Notes |
|--------|---------------------|--------------------|------------|-------|
| BBC | ✅ | ✅ | ❌ defuddle fails | Use browser first, Google fallback |
| Al Jazeera | ✅ | ✅ | ✅ sometimes | Date-based slug usually works |
| Reuters | ❌ bot blocked | ✅ | ❌ fails | Google News only |
| AP News | ❌ | ✅ | ❌ likely fails | Use Google News |
| NYTimes | ❌ paywall/403 | ✅ | ❌ | Google News only |
| The Guardian | ✅ | ✅ | ❌ 403 | Google News works |
| DW.com | ✅ | ✅ | ✅ | Works direct usually |

**Rule of thumb:** If direct URL fails, use Google News to find the canonical. Never spend more than 2 attempts on a single story before switching to Google News.