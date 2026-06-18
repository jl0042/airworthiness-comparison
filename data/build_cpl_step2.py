#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 2: insert cpl_article / cpl_page / cpl_title / cpl_observation columns into
airworthiness_mapping.csv, right after the upl_* columns. cpl_* clause fields are
filled mechanically by matching each row's topic `code` to CPL.<code> (the CPL
numbering mirrors UPL). cpl_observation is left blank here and filled by the
Workflow diff stage. Idempotent: re-running rewrites the same columns.
"""
import csv, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, 'data', 'airworthiness_mapping.csv')
BODIES = json.load(open(os.path.join(ROOT, 'data', 'clause_bodies.json'), encoding='utf-8'))

NEW_COLS = ['cpl_article', 'cpl_page', 'cpl_title']

def main():
    with open(MAP, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    header, data = rows[0], rows[1:]

    # strip any prior run's cpl_* columns so re-runs stay clean
    keep = [i for i, h in enumerate(header) if h not in NEW_COLS]
    header = [header[i] for i in keep]
    data = [[r[i] for i in keep] for r in data]

    upl_idx = header.index('upl_title')
    insert_at = upl_idx + 1
    header[insert_at:insert_at] = NEW_COLS

    code_idx = header.index('code')
    matched = 0
    for r in data:
        code = r[code_idx].strip()
        art = 'CPL.' + code
        if art in BODIES:
            e = BODIES[art]
            cpl = [art, str(e['page']), e['title']]
            matched += 1
        else:
            cpl = ['', '', '']
        r[insert_at:insert_at] = cpl

    with open(MAP, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(data)

    print(f'rows: {len(data)} | cpl matched: {matched} | blank: {len(data)-matched}')
    print('header:', header)


if __name__ == '__main__':
    main()
