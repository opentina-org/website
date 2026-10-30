#!/usr/bin/env python3
"""内容层翻译审计：章节结构、仓库清单、未译段落残留。"""
import glob
import os
import re

LANGS = ["en", "zh", "zh-tw", "ja", "ru", "ko", "de", "fr", "es"]
CJK = re.compile(r"[\u4e00-\u9fff]")
KANA = re.compile(r"[\u3040-\u30ff]")
HANGUL = re.compile(r"[\uac00-\ud7af]")
CYR = re.compile(r"[\u0400-\u04ff]")


def load(lang, name):
    p = f"content/{lang}/{name}"
    if not os.path.exists(p):
        return None
    return open(p, encoding="utf-8").read()


def strip_fm(t):
    if t.startswith("---"):
        parts = t.split("---", 2)
        return parts[2] if len(parts) > 2 else ""
    return t


def stats(text):
    body = strip_fm(text)
    heads = re.findall(r"^(#{2,6})\s+(.*)$", body, re.M)
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", body)
    repos = sorted({m for m in re.findall(r"github\.com/opentina-org/([A-Za-z0-9._-]+)", body)})
    return heads, links, repos


print("== 结构对比（about / docs：标题数 / 外链数 / 仓库清单）==")
for name in ["about.md", "docs.md"]:
    print(f"-- {name} --")
    en_heads, en_links, en_repos = stats(load("en", name))
    for lang in LANGS:
        t = load(lang, name)
        if t is None:
            print(f"   {lang:6s} 缺文件")
            continue
        h, l, r = stats(t)
        flags = []
        if len(h) != len(en_heads):
            flags.append(f"标题 {len(h)}≠{len(en_heads)}")
        if len(l) != len(en_links):
            flags.append(f"链接 {len(l)}≠{len(en_links)}")
        if r != en_repos:
            flags.append(f"仓库差异 {set(r) ^ set(en_repos)}")
        print(f"   {lang:6s} 标题 {len(h)} 链接 {len(l)} 仓库 {len(r)} {' | '.join(flags) if flags else 'OK'}")

print()
print("== 未译段落扫描（非拉丁语言里的纯拉丁句子）==")
for lang in ["zh", "zh-tw", "ja", "ru", "ko"]:
    for name in ["about.md", "docs.md"]:
        t = load(lang, name)
        if not t:
            continue
        body = strip_fm(t)
        hits = []
        for para in [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]:
            if para.startswith(("#", "|", "```", ">", "-", "*", "1.", "2.", "3.", "4.")):
                continue
            letters = re.sub(r"[^A-Za-z]", "", para)
            if len(letters) < 40:
                continue
            native = CJK.search(para) or KANA.search(para) or HANGUL.search(para) or CYR.search(para)
            if not native:
                hits.append(para[:110].replace("\n", " "))
        if hits:
            print(f"   {lang}/{name}: {len(hits)} 段疑似未译")
            for h in hits[:3]:
                print(f"      · {h}")
