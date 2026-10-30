#!/usr/bin/env python3
"""检查 i18n/*.toml 的键覆盖与未翻译残留。"""
import glob
import os
import re
import sys

LANGS = ["en", "zh", "zh-tw", "ja", "ru", "ko", "de", "fr", "es"]


def parse(path):
    d = {}
    key = None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"^\[([^\]]+)\]", line)
        if m:
            key = m.group(1)
            continue
        m = re.match(r'^\s*other\s*=\s*"(.*)"\s*$', line)
        if m and key:
            d[key] = m.group(1)
    return d


data = {}
for lang in LANGS:
    p = f"i18n/{lang}.toml"
    if not os.path.exists(p):
        print(f"缺少 {p}")
        continue
    data[lang] = parse(p)

base = data["en"]
print(f"基准 en: {len(base)} 键")
print()
for lang in LANGS:
    if lang == "en" or lang not in data:
        continue
    d = data[lang]
    missing = [k for k in base if k not in d]
    extra = [k for k in d if k not in base]
    same = [k for k in base if k in d and d[k].strip() == base[k].strip()]
    print(f"== {lang}: {len(d)} 键 | 缺 {len(missing)} | 多 {len(extra)} | 与英文完全相同 {len(same)}")
    for k in missing:
        print(f"     缺键: {k}")
    for k in extra:
        print(f"     多余: {k}")
    for k in same:
        print(f"     未译?: [{k}] {base[k][:70]}")
print()
print("== 全站内容文件覆盖 ==")
for lang in LANGS:
    files = sorted(glob.glob(f"content/{lang}/*.md"))
    names = [os.path.basename(f) for f in files]
    need = ["_index.md", "about.md", "docs.md"]
    miss = [n for n in need if n not in names]
    print(f"  {lang:6s} {len(files)} 文件 {names} {'缺: ' + str(miss) if miss else ''}")
