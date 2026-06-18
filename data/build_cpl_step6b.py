#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 6b: add the 载人/不载人 主线观察 (fifth point) to the summary card, using the
synthesized + verified mainObs. Inserts a <h5> heading + the 3 paragraphs before
the card's source line. Applied to data/summary_fragment.html then swapped into
the verbatim copy in index.html.
"""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAG = os.path.join(ROOT, 'data', 'summary_fragment.html')
INDEX = os.path.join(ROOT, 'index.html')

mainobs = open('/tmp/cpl_main_obs.html', encoding='utf-8').read().strip()
# drop the synthesized source line; the card has its own source which we extend
mainobs_body = re.sub(r'<div class="source">.*?</div>\s*$', '', mainobs, flags=re.S).strip()

HEADING = ('<h5 style="font-family:var(--font-serif-zh);font-size:15px;font-weight:600;'
           'color:var(--ink);margin:14px 0 6px">五  45 号载人标准 — 把删掉的有人机条款逐条补回</h5>')

SECTION = HEADING + '\n' + mainobs_body + '\n'

SRC_EXTRA = ' 第五点「载人 / 不载人」对照引 AC-21-AA-2026-45《动力提升航空器适航标准》PDF 正文, 与 AC-21-AA-2026-47 (UPL) 同号条款逐条横向核对。'


def main():
    frag = open(FRAG, encoding='utf-8').read()
    orig = frag

    src_m = re.search(r'<div class="source">(.*?)</div>', frag, re.S)
    assert src_m, 'source div not found'
    # insert section before the source div
    frag = frag[:src_m.start()] + SECTION + '\n  ' + frag[src_m.start():]
    # extend the source line
    frag = frag.replace('<div class="source">' + src_m.group(1) + '</div>',
                        '<div class="source">' + src_m.group(1) + SRC_EXTRA + '</div>', 1)

    open(FRAG, 'w', encoding='utf-8').write(frag)

    idx = open(INDEX, encoding='utf-8').read()
    assert orig.strip() in idx, 'summary_fragment not verbatim in index.html'
    idx = idx.replace(orig.strip(), frag.strip(), 1)
    open(INDEX, 'w', encoding='utf-8').write(idx)
    print('added 五 (载人/不载人) section to summary card')


if __name__ == '__main__':
    main()
