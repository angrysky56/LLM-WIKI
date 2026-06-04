#!/usr/bin/env python3
"""Print full descriptions of the top candidate stories."""
import json
with open('/home/ty/Documents/LLM-WIKI/wiki/scratchpad/agent-sheets/news/workspace/rss_2026-06-04.json') as f:
    data = json.load(f)

# Top candidates to inspect
keywords = {
    'us_house_iran_war_powers': 'halt Iran war',
    'israel_lebanon_ceasefire': 'Israel and Lebanon agree to implement ceasefire',
    'kim_nuclear_expansion': "Kim Jong Un calls for",
    'hezbollah_fiber_optic': 'Fiber-Optic Drones',
    'smotrich_west_bank_homes': '2,162 homes',
    'india_monsoon_late': 'monsoon',
    'argentina_protest_teen': 'Argentina erupts in protest',
    'meta_australia_news': 'Meta slams Australia',
    'screwworm_parasite_us': 'Screwworm',
    'dr_congo_ebola_january': 'Ebola outbreak could have begun',
    'kenya_ebola_centre': 'American-only Ebola quarantine',
    'priest_ebola_death_drc': "Priest's Ebola Death",
    'us_house_iran_rebuke_alts': 'rebuke to Trump',
    'iraq_drones': 'IRH',
    'somalia_mogadishu_clashes': 'Mogadishu',
    'nz_lawmakers_china_taiwan': 'New Zealand Lawmakers Banned From China',
    'abudhabi_zambia_copper': 'IRH Turns Down Zambian Copper',
    'korea_local_elections': "Democratic Party Sweeps Local Elections",
    'germany_un_russia_defeat': "Germany blames Russia",
    'espriella_colombia_us_citizen': 'Can Abelardo De La Espriella, a U.S. Citizen',
    'crypto_kidnapping_mexico': 'Kidnappings, threats',
    'cocaine_tunnel_us_mexico': 'cocaine bust',
    'irish_defense': 'Ireland',
    'trump_blanche_attorney': 'Blanche for attorney general',
    'goldman_ms_ipo': 'Goldman Erects Lobby Rockets',
    'eu_trading_book': 'EU Delays Trading-Book',
    'broadcom_ai': 'Broadcom',
    'oil_falls_ceasefire': 'Oil Falls After Israel-Lebanon',
    'japan_plastic_shortage': 'naphtha shortage',
    'kim_world_cup': 'Soccer Leader',
}

seen = set()
print('=' * 80)
print('FULL DESCRIPTIONS OF CANDIDATE STORIES')
print('=' * 80)
for feed_name, info in data.items():
    for s in info.get('stories', []):
        title = s['title']
        for k, kw in keywords.items():
            if kw in title and (feed_name, k) not in seen:
                seen.add((feed_name, k))
                print(f'\n--- [{feed_name}] {k} ---')
                print(f'TITLE: {title}')
                print(f'PUB:   {s["pubDate"]}')
                print(f'LINK:  {s["link"]}')
                print(f'DESC:  {s["description"]}')
                print('-' * 80)
                break
