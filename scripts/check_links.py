#!/usr/bin/env python3
"""OpenTina 站点内部链接检查器。

用法:
  python3 check_links.py public            # 只查本地构建产物
  python3 check_links.py public --live     # 再对线上 https://opentina.org 逐条实测
"""
import os
import re
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

ROOT = sys.argv[1] if len(sys.argv) > 1 else "public"
LIVE = "--live" in sys.argv
BASE = "https://opentina.org"

HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
SCRIPT = re.compile(r"<script.*?</script>", re.S | re.I)
STYLE = re.compile(r"<style.*?</style>", re.S | re.I)
ATTR = re.compile(r"""(?:href|src)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>"']+))""", re.I)


def attr_value(m):
    return next(g for g in m.groups() if g is not None)


def pages():
    for dirpath, _, files in os.walk(ROOT):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(dirpath, f)


def local_target(url_path):
    p = url_path.split("#")[0].split("?")[0]
    if not p.startswith("/"):
        return None
    cand = os.path.join(ROOT, p.lstrip("/"))
    if p.endswith("/"):
        return os.path.join(cand, "index.html")
    return cand


def collect():
    rows = []
    for f in pages():
        html = open(f, encoding="utf-8", errors="replace").read()
        html = HTML_COMMENT.sub("", html)
        html = SCRIPT.sub("", html)
        html = STYLE.sub("", html)
        for m in ATTR.finditer(html):
            href = attr_value(m).strip()
            if not href or href.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
                continue
            src = "/" + os.path.relpath(f, ROOT)
            rows.append((src, href))
    return rows


def main():
    rows = collect()
    locals_, externals = [], []
    for src, href in rows:
        if href.startswith(BASE):
            locals_.append((src, href[len(BASE):] or "/"))
        elif href.startswith(("http://", "https://", "//")):
            externals.append((src, href))
        elif href.startswith("/"):
            locals_.append((src, href))
        else:
            base = os.path.dirname(src)
            joined = os.path.normpath(os.path.join(base, href.split("#")[0])).replace(os.sep, "/")
            if not joined.startswith("/"):
                joined = "/" + joined
            locals_.append((src, joined))

    uniq = sorted({h for _, h in locals_})
    broken = [h for h in uniq if not os.path.exists(local_target(h) or "")]
    print(f"页面数: {sum(1 for _ in pages())}")
    print(f"站内链接引用: {len(locals_)} 次 / 去重 {len(uniq)} 个目标")
    print(f"外链引用: {len(externals)} 次（去重 {len({h for _, h in externals})} 个）")
    print()
    if broken:
        print(f"[FAIL] 本地构建中不可达的站内目标: {len(broken)}")
        for b in broken:
            srcs = sorted({s for s, h in locals_ if h == b})
            print(f"   {b}   <- 出现在 {len(srcs)} 个页面: {', '.join(srcs[:4])}")
    else:
        print("[OK] 本地构建：站内目标全部可达")

    if LIVE:
        print()
        print("== 线上实测 ==")

        def check(path):
            r = subprocess.run(
                ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-m", "25", BASE + path],
                capture_output=True, text=True)
            return path, r.stdout.strip()

        with ThreadPoolExecutor(max_workers=8) as ex:
            res = list(ex.map(check, uniq))
        bad = [(p, c) for p, c in res if c != "200"]
        if bad:
            print(f"[FAIL] 线上不可达: {len(bad)}/{len(res)}")
            for p, c in sorted(bad):
                print(f"   {c}  {BASE}{p}")
        else:
            print(f"[OK] 线上 {len(res)} 个站内目标全部 200")


if __name__ == "__main__":
    main()
