"""Validate the built site, links, metadata, and publication boundaries."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

from articles import ARTICLES

ROOT = Path(__file__).resolve().parent / "dist"
BASE = "https://energi.vijeron.com"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags: list[tuple[str, dict[str, str]]] = []
        self.h1 = 0
        self.jsonld = False

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append((tag, data))
        if tag == "h1":
            self.h1 += 1
        if tag == "script" and data.get("type") == "application/ld+json":
            self.jsonld = True


def local_target(href: str) -> Path | None:
    if not href.startswith("/") or href.startswith("//"):
        return None
    path = urlsplit(href).path
    return ROOT / (path.lstrip("/") + "index.html" if path.endswith("/") else path.lstrip("/"))


def check() -> None:
    pages = sorted(ROOT.rglob("*.html"))
    assert len(pages) == 33, f"expected 32 public pages and 404, got {len(pages)}"
    for file in pages:
        raw = file.read_text(encoding="utf-8")
        if file.name == "404.html":
            continue
        page = Page()
        page.feed(raw)
        rel = file.relative_to(ROOT).as_posix().removesuffix("index.html")
        url = BASE + "/" + rel if rel else BASE + "/"
        lang = "en" if rel.startswith("en/") else "id"
        assert page.h1 == 1, f"one h1 required: {file}"
        assert page.jsonld, f"missing JSON-LD: {file}"
        assert f'<html lang=\'{lang}\'>' in raw, f"language mismatch: {file}"
        assert f"<link rel='canonical' href='{url}'>" in raw, f"canonical mismatch: {file}"
        assert raw.count("hreflang=") == 3, f"incomplete language alternates: {file}"
        if any(section in rel for section in ("privasi/", "tentang/", "metode/")):
            assert "pagead2.googlesyndication.com" not in raw
            assert "vijeron-ads.js" not in raw
        else:
            assert "ca-pub-6180580801533680" in raw
            assert raw.index("gtag('consent','default'") < raw.index("gtag('config'")
        for tag, attrs in page.tags:
            if tag not in ("a", "link", "script"):
                continue
            target = attrs.get("href") or attrs.get("src")
            if not target:
                continue
            local = local_target(target)
            assert local is None or local.exists(), f"broken local link {target} in {file}"
    tree = ElementTree.parse(ROOT / "sitemap.xml")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [node.text for node in tree.findall("s:url/s:loc", ns)]
    assert len(urls) == 32 and len(set(urls)) == 32
    assert len(ARTICLES) == 10
    assert (ROOT / "robots.txt").read_text().find("sitemap.xml") >= 0
    print(f"PASS: {len(urls)} canonical pages, {len(ARTICLES)} bilingual guides, links, sitemap, tags")


if __name__ == "__main__":
    try:
        check()
    except AssertionError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
