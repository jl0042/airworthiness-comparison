#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 5: splice CPL clause-blocks into the 逐条对比 detail tables.

For every detail-table <tr> whose topic code has a CPL.<code> clause, insert a
CPL clause-block (mirroring the UPL block markup) into the 4th cell — the 载人
eVTOL column (relabelled from 载客 eVTOL 专用 (PEU)). CPL is listed before the
PEU special-condition block. The transform is applied to data/detail_fragment.html
and the identical inlined region is swapped into index.html, keeping them in sync.
"""
import re, json, os, urllib.parse, html as _html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAG = os.path.join(ROOT, 'data', 'detail_fragment.html')
INDEX = os.path.join(ROOT, 'index.html')
BODIES = json.load(open(os.path.join(ROOT, 'data', 'clause_bodies.json'), encoding='utf-8'))

PDF_NAME = 'AC-21-AA-2026-45动力提升航空器适航标准.pdf'
PDF_HREF = '适航标准/' + urllib.parse.quote(PDF_NAME)

# header relabels (also widen the eVTOL column, clarify 不载人/载人 split)
HEADER_REPLACES = [
    ('<th style="width:27%">成熟有人机 (CCAR-23 / 27)</th>',
     '<th style="width:25%">成熟有人机 (CCAR-23 / 27)</th>'),
    ('<th style="width:26%">正常类无人机 (UMR / UPL / AEC)</th>',
     '<th style="width:23%">正常类·不载人 (UMR / UPL / AEC)</th>'),
    ('<th style="width:17%">载客 eVTOL 专用 (PEU)</th>',
     '<th style="width:22%">载人 eVTOL (CPL 标准 / PEU 专条)</th>'),
]

CODE_RE = re.compile(r'(?:UMR|UPL)\.([A-Z]?\d{3,4})|(?<![\d.])23\.(\d{3,4})')
DASH_CELL_RE = re.compile(r'^\s*<span[^>]*>—</span>\s*$')


def esc(s):
    # match existing style: raw text, only escape the structural chars
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def cpl_block(code):
    art = 'CPL.' + code
    e = BODIES[art]
    title = esc(e['title'])
    first = esc(e['first_para'])
    href = f'{PDF_HREF}#page={e["page"]}'
    b = (f'<div class="clause-block"><b>{art}</b> {title} '
         f'<sup class="pdfref"><a href="{href}" target="_blank">📄p.{e["page"]}</a></sup>'
         f'<div class="clause-first">{first}</div>')
    if e['full'].replace('\n', ' ') != e['first_para']:
        b += (f'<details class="clause-more" data-clause-id="{art}">'
              f'<summary>展开完整原文 ({e["subitem_count"]} 子项 / {e["char_count"]} 字)</summary>'
              f'<div class="clause-full" data-pending="1"></div></details>')
    b += '</div>'
    return b


def row_code(row_html):
    for m in CODE_RE.finditer(row_html):
        code = m.group(1) or m.group(2)
        if 'CPL.' + code in BODIES:
            return code
    return None


def transform_row(row_html):
    code = row_code(row_html)
    if not code:
        return row_html, False
    cells = re.findall(r'<td[^>]*>.*?</td>', row_html, re.S)
    if len(cells) != 5:
        return row_html, False
    target = cells[3]
    inner = re.match(r'(<td[^>]*>)(.*)(</td>)', target, re.S)
    open_tag, content, close_tag = inner.group(1), inner.group(2), inner.group(3)
    block = cpl_block(code)
    if DASH_CELL_RE.match(content):
        new_content = block
    else:
        new_content = block + content
    new_cell = open_tag + new_content + close_tag
    new_row = row_html.replace(target, new_cell, 1)
    return new_row, True


def main():
    frag = open(FRAG, encoding='utf-8').read()
    orig_frag = frag

    for a, b in HEADER_REPLACES:
        assert a in frag, f'header not found: {a}'
        frag = frag.replace(a, b)

    # split into rows, transform each, reassemble
    parts = re.split(r'(<tr[^>]*>.*?</tr>)', frag, flags=re.S)
    count = 0
    for i, p in enumerate(parts):
        if p.startswith('<tr'):
            new, changed = transform_row(p)
            if changed:
                parts[i] = new
                count += 1
    frag = ''.join(parts)

    open(FRAG, 'w', encoding='utf-8').write(frag)

    # swap the identical region inside index.html
    idx = open(INDEX, encoding='utf-8').read()
    assert orig_frag.strip() in idx, 'original detail fragment not found verbatim in index.html'
    idx = idx.replace(orig_frag.strip(), frag.strip(), 1)
    open(INDEX, 'w', encoding='utf-8').write(idx)

    print(f'CPL blocks inserted into {count} rows')


if __name__ == '__main__':
    main()
