#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Step 4: add the CPL column (index 9) to the heatmap. Appends "CPL" to `models`,
adds 9 tooltip entries "9,0".."9,8", and 9 series triples [9,row,severity], using
the verified per-dimension analysis in /tmp/cpl_dims_final.json. Applied to
data/matrix.js then the verbatim copy is swapped into index.html.
"""
import re, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATRIX = os.path.join(ROOT, 'data', 'matrix.js')
INDEX = os.path.join(ROOT, 'index.html')
DIMS = {d['dim_index']: d for d in json.load(open('/tmp/cpl_dims_final.json'))['dims']}

COL = 9  # new model column index


def transform(js):
    # dims list (y-axis names)
    dims = json.loads(re.search(r'const dims = (\[.*?\]);', js, re.S).group(1))
    assert len(dims) == 9

    # 1) models: append CPL
    models_m = re.search(r'(const models = )(\[.*?\])(;)', js, re.S)
    models = json.loads(models_m.group(2))
    assert models[-1] == 'HY' and 'CPL' not in models
    models.append('CPL')
    js = js[:models_m.start()] + models_m.group(1) + json.dumps(models, ensure_ascii=False) + models_m.group(3) + js[models_m.end():]

    # 2) tooltips: add 9 entries
    tip_m = re.search(r'(const tooltips = )(\{.*?\})(;)', js, re.S)
    tips = json.loads(tip_m.group(2))
    for r in range(9):
        d = DIMS[r]
        tips[f'{COL},{r}'] = {'model': 'CPL', 'dim': dims[r], 'color': d['color'], 'tooltip': d['tooltip']}
    js = js[:tip_m.start()] + tip_m.group(1) + json.dumps(tips, ensure_ascii=False) + tip_m.group(3) + js[tip_m.end():]

    # 3) series data: append 9 triples
    data_m = re.search(r'(data:\s*)(\[\[.*?\]\])', js, re.S)
    data = json.loads(data_m.group(2))
    assert not any(t[0] == COL for t in data)
    for r in range(9):
        data.append([COL, r, DIMS[r]['severity']])
    js = js[:data_m.start()] + data_m.group(1) + json.dumps(data) + js[data_m.end():]

    return js


def main():
    js = open(MATRIX, encoding='utf-8').read()
    orig = js
    js = transform(js)
    open(MATRIX, 'w', encoding='utf-8').write(js)

    idx = open(INDEX, encoding='utf-8').read()
    assert orig.strip() in idx, 'matrix.js not verbatim in index.html'
    idx = idx.replace(orig.strip(), js.strip(), 1)
    open(INDEX, 'w', encoding='utf-8').write(idx)

    print('heatmap: appended CPL column (models/tooltips/series)')
    print('CPL severities by dim:', [DIMS[r]['severity'] for r in range(9)])


if __name__ == '__main__':
    main()
