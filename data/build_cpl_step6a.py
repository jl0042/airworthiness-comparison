#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 6a: weave the verified per-dimension CPL (载人) note into each of the 9
dimension cards (.dim-obs), mirroring how UMR/UPL are discussed. Applied to
data/dimensions_fragment.html then swapped into the verbatim copy in index.html.
"""
import re, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAG = os.path.join(ROOT, 'data', 'dimensions_fragment.html')
INDEX = os.path.join(ROOT, 'index.html')
DIMS = {d['dim_index']: d for d in json.load(open('/tmp/cpl_dims_final.json'))['dims']}

LABEL = '<b style="color:var(--accent)">＋ 45 号 CPL（载人）</b> '
WRAP_OPEN = '<span style="display:block;margin-top:7px;padding-top:6px;border-top:1px dashed var(--gray-5)">'
WRAP_CLOSE = '</span>'


def addendum_html(i):
    txt = DIMS[i]['card_addendum']
    # avoid redundancy with the label
    txt = re.sub(r'^载人\s*CPL\s*', '', txt)
    return WRAP_OPEN + LABEL + txt + WRAP_CLOSE


def main():
    frag = open(FRAG, encoding='utf-8').read()
    orig = frag

    # 9 dim-obs blocks in dim order 0..8
    blocks = list(re.finditer(r'<div class="dim-obs">.*?</div>', frag, re.S))
    assert len(blocks) == 9, f'expected 9 dim-obs, got {len(blocks)}'

    # rebuild back-to-front so offsets stay valid
    out = frag
    for i in range(8, -1, -1):
        m = blocks[i]
        insert_at = m.end() - len('</div>')
        out = out[:insert_at] + addendum_html(i) + out[insert_at:]
    frag = out

    open(FRAG, 'w', encoding='utf-8').write(frag)

    idx = open(INDEX, encoding='utf-8').read()
    assert orig.strip() in idx, 'dimensions_fragment not verbatim in index.html'
    idx = idx.replace(orig.strip(), frag.strip(), 1)
    open(INDEX, 'w', encoding='utf-8').write(idx)

    print(f'appended CPL note to 9 dimension cards')


if __name__ == '__main__':
    main()
