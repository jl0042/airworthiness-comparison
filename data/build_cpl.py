#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 1 of the CPL integration: extract clauses from AC-21-AA-2026-45
《动力提升航空器适航标准》(CPL, crewed powered-lift) and produce
  - data/clauses_cpl.csv          (same schema as clauses_upl.csv)
  - CPL.* entries merged into data/clause_bodies.json

Mirrors the documented pipeline (PyMuPDF + cross-page lookahead) used for the
existing UMR / UPL / CCAR standards. Pure extraction from the source PDF — no
interpretation. Run from repo root.
"""
import fitz, re, csv, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, '适航标准', 'AC-21-AA-2026-45动力提升航空器适航标准.pdf')
BODY_START = 12  # 0-based; page 13 = first 附件1 body page (A 章总则 / CPL.2000)

# --- punctuation normalisation: match existing clause_bodies.json style ---
def normalize(s):
    return (s.replace('（', '(').replace('）', ')')
             .replace('，', ',').replace('；', ';').replace('：', ':'))

CHAP_RE   = re.compile(r'^[A-Z]\s*章')                       # A 章总则 / H 章电动发动机
SEC_RE    = re.compile(r'^第[一二三四五六七八九十]+节')          # 第一节性能
APPX_RE   = re.compile(r'^附录[A-Z]')                         # 附录A 持续适航文件
FOOT_RE   = re.compile(r'^[—\-－–]+\s*\d*\s*[—\-－–]*$')      # — 5 — page footers
ANCHOR_RE = re.compile(r'^CPL\.([A-Z]?\d{1,4})\s*条?\s*(.*)$')  # CPL.2100条重量和重心
MARK_RE   = re.compile(r'^\([0-9a-zA-Z一二三四五六七八九十]{1,4}\)')  # (a) (1) (一) (i)

def main():
    d = fitz.open(PDF)

    # gather body lines tagged with their 1-based PDF page
    lines = []
    for i in range(BODY_START, d.page_count):
        for ln in d[i].get_text().split('\n'):
            lines.append((i + 1, ln))

    clauses = []
    cur = None
    subpart = ''
    for page, raw in lines:
        ln = normalize(raw).strip()
        if not ln:
            continue
        if FOOT_RE.match(ln):
            continue
        if '编制说明' in ln:        # 附录 clauses end here; rest is drafting notes
            break
        if ln.startswith('附件'):
            continue
        if APPX_RE.match(ln):
            subpart = '附录'
            continue
        if CHAP_RE.match(ln):
            subpart = ln[0]            # chapter letter A..I
            continue
        if SEC_RE.match(ln):
            continue
        m = ANCHOR_RE.match(ln)
        if m:
            cur = {'article': 'CPL.' + m.group(1),
                   'subpart': subpart,
                   'page': page,
                   'title': m.group(2).strip(),
                   'lines': []}
            clauses.append(cur)
            continue
        if cur is not None:
            cur['lines'].append(ln)

    # de-dup: keep first occurrence of each article (guards against stray repeats)
    seen = {}
    ordered = []
    for c in clauses:
        if c['article'] in seen:
            continue
        seen[c['article']] = True
        ordered.append(c)
    clauses = ordered

    bodies = {}
    csv_rows = []
    for c in clauses:
        # rebuild subitems: new segment at each marker line, wrapped lines joined by space
        segs = []
        for ln in c['lines']:
            if MARK_RE.match(ln) or not segs:
                segs.append(ln)
            else:
                segs[-1] += ' ' + ln
        full = '\n'.join(segs).strip()
        title = c['title']
        # title fallback: if title empty, first non-marker seg becomes title
        if not title and segs and not MARK_RE.match(segs[0]):
            title = segs[0]
            full = '\n'.join(segs[1:]).strip()
        subitem_count = sum(1 for s in segs if MARK_RE.match(s))
        char_count = len(full)
        # first_para: greedy subitems joined by space, <=150 chars
        fp = ''
        for s in full.split('\n'):
            cand = s if not fp else fp + ' ' + s
            if fp and len(cand) > 150:
                break
            fp = cand
        bodies[c['article']] = {
            'first_para': fp,
            'full': full,
            'subitem_count': subitem_count,
            'char_count': char_count,
            'page': c['page'],
            'title': title,
        }
        csv_rows.append((c['subpart'], c['article'], c['page'], title))

    # --- write clauses_cpl.csv (BOM + same header as clauses_upl.csv) ---
    with open(os.path.join(ROOT, 'data', 'clauses_cpl.csv'), 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f)
        w.writerow(['standard', 'subpart', 'article', 'pdf_page', 'title_raw'])
        for sub, art, pg, title in csv_rows:
            w.writerow(['CPL', sub, art, pg, title])

    # --- merge CPL.* into clause_bodies.json ---
    jpath = os.path.join(ROOT, 'data', 'clause_bodies.json')
    existing = json.load(open(jpath, encoding='utf-8'))
    before = len(existing)
    existing.update(bodies)
    json.dump(existing, open(jpath, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

    print(f'extracted {len(clauses)} CPL clauses')
    print(f'clause_bodies.json: {before} -> {len(existing)} keys (+{len(existing)-before})')
    print('subparts:', sorted(set(r[0] for r in csv_rows)))
    # sample
    for k in ['CPL.2000', 'CPL.2100', 'CPL.2600', 'CPL.3304']:
        if k in bodies:
            e = bodies[k]
            print(f"  {k} p{e['page']} '{e['title']}' {e['subitem_count']}子项/{e['char_count']}字")


if __name__ == '__main__':
    main()
