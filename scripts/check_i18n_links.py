#!/usr/bin/env python3
"""验证语言切换器与 hreflang：每个页面 × 每种语言的跳转目标都必须在构建产物中存在。"""
import glob
import os
import re
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "public"
LANGS = ["en", "zh", "zh-tw", "ja", "ru", "ko", "de", "fr", "es"]

A_HREF = re.compile(r'<a [^>]*hreflang=([a-zA-Z-]+)[^>]*href=([^ >]+)[^>]*>([^<]+)</a>')
HEAD_HL = re.compile(r'<link rel=alternate hreflang=([a-zA-Z-]+) href=([^ >]+)>')


def target_ok(url):
    p = url.replace("https://opentina.org", "").split("#")[0] or "/"
    f = os.path.join(ROOT, p.lstrip("/"))
    if p.endswith("/"):
        f = os.path.join(f, "index.html")
    return os.path.exists(f), p


def main():
    pages = [p for p in glob.glob(f"{ROOT}/**/*.html", recursive=True)
             if not p.endswith("404.html")]
    # 排除跳转存根（Hugo 为默认语言生成的 /en/ -> / 转跳页，无站点骨架）
    pages = [p for p in pages
             if "http-equiv=refresh" not in open(p, encoding="utf-8", errors="replace").read(600)]
    print(f"检查页面: {len(pages)}")
    switch_bad, head_bad, cur_bad = [], [], []
    for f in sorted(pages):
        html = open(f, encoding="utf-8", errors="replace").read()
        body = html.split("</head>", 1)[1] if "</head>" in html else html
        menu = A_HREF.findall(body)
        if len(menu) < len(LANGS):
            switch_bad.append((f, f"仅 {len(menu)} 条语言链接"))
        for lang, href, _ in menu:
            ok, p = target_ok(href)
            if not ok:
                switch_bad.append((f, f"{lang} -> {p} 不存在"))
        cur = [t for t in menu if 'class=current' in ""]
        hls = HEAD_HL.findall(html)
        codes = {l for l, _ in hls if l != "x-default"}
        if len(codes) < len(LANGS):
            head_bad.append((f, sorted(codes)))
        if not any(l == "x-default" for l, _ in hls):
            head_bad.append((f, "缺 x-default"))
        for lang, href in hls:
            if lang == "x-default":
                continue
            ok, p = target_ok(href)
            if not ok:
                head_bad.append((f, f"hreflang {lang} -> {p} 不存在"))

    if switch_bad:
        print(f"[FAIL] 语言切换器问题 {len(switch_bad)}")
        for f, m in switch_bad[:12]:
            print(f"   {f}: {m}")
    else:
        print("[OK] 所有页面的语言切换器目标均存在，且 9 种语言齐全")

    if head_bad:
        print(f"[FAIL] hreflang 问题 {len(head_bad)}")
        for f, m in head_bad[:12]:
            print(f"   {f}: {m}")
    else:
        print("[OK] 所有页面 hreflang 覆盖 9 种语言 + x-default，且目标存在")


if __name__ == "__main__":
    main()
