#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 6c: add the 载人 CPL row to the 分级矩阵 (categorization). Inserts a row right
after the 不载人 UPL 动力提升 row, in the 复合翼/动力提升 group, and bumps the source
count 12 -> 13. Applied to data/categorization_fragment.html then swapped into the
verbatim copy in index.html. Also appends a row to airworthiness_categorization.csv.
"""
import re, os, csv, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAG = os.path.join(ROOT, 'data', 'categorization_fragment.html')
INDEX = os.path.join(ROOT, 'index.html')
CSVF = os.path.join(ROOT, 'data', 'airworthiness_categorization.csv')

PDF_REL = '适航标准/' + urllib.parse.quote('AC-21-AA-2026-45动力提升航空器适航标准.pdf')

UPL_ROW_ANCHOR = '<td><span style="color:var(--ink)">峰飞 V2000CG (走 SC 路径; UPL 出之前已 2024-03 TC)</span></td></tr>'

CPL_ROW = (
    '<tr style="background:rgba(184,88,74,.10)">'
    '<td></td><td>中大型(≤5700kg)</td><td>正常类·<b>载人</b></td>'
    '<td>动力提升航空器适航标准 (载人 eVTOL) '
    f'<sup class="pdfref"><a href="{PDF_REL}" target="_blank">📄</a></sup></td>'
    '<td><span style="display:inline-block;font-family:var(--font-mono);font-size:9.5px;padding:2px 7px;'
    'border-radius:3px;background:var(--accent);color:var(--paper);letter-spacing:.5px">已发布</span>'
    '<br><span style="color:var(--gray-3);font-size:10px;font-family:var(--font-mono)">2026-02-12</span></td>'
    '<td><span style="color:var(--gray-3)">无 (在研)</span></td></tr>'
)


def main():
    frag = open(FRAG, encoding='utf-8').read()
    orig = frag
    assert UPL_ROW_ANCHOR in frag, 'UPL 动力提升 row anchor not found'
    assert CPL_ROW not in frag, 'CPL row already present'
    frag = frag.replace(UPL_ROW_ANCHOR, UPL_ROW_ANCHOR + CPL_ROW, 1)
    frag = frag.replace('12 份 CAAC 适航 PDF 封页', '13 份 CAAC 适航 PDF 封页', 1)

    open(FRAG, 'w', encoding='utf-8').write(frag)

    idx = open(INDEX, encoding='utf-8').read()
    assert orig.strip() in idx, 'categorization_fragment not verbatim in index.html'
    idx = idx.replace(orig.strip(), frag.strip(), 1)
    open(INDEX, 'w', encoding='utf-8').write(idx)

    # append a row to the source CSV (mirror the new category)
    with open(CSVF, encoding='utf-8-sig', newline='') as f:
        rows = list(csv.reader(f))
    header = rows[0]
    new = {h: '' for h in header}
    new.update({
        header[0]: '复合翼/动力提升', header[1]: '中大型(≤5700kg)', header[2]: '正常类·载人',
        '适用文件': '动力提升航空器适航标准 (载人 eVTOL)',
        '文件相对路径': '适航标准/AC-21-AA-2026-45动力提升航空器适航标准.pdf',
        '状态': '已发布', '颁布日期': '2026-02-12', '编号': 'AC-21-AA-2026-45',
        '已取TC型号': '无 (在研)',
    })
    if not any(r and r[header.index('编号')] == 'AC-21-AA-2026-45' for r in rows[1:] if len(r) > header.index('编号')):
        with open(CSVF, 'a', encoding='utf-8-sig', newline='') as f:
            csv.writer(f).writerow([new.get(h, '') for h in header])

    print('added 载人 CPL row to categorization (fragment + index + csv)')


if __name__ == '__main__':
    main()
