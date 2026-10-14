#!/usr/bin/env python3
"""Find and fetch freely licensed photos from Wikimedia Commons for articles.

  search "<query>" [n]          list candidates: file title, licence, author, size
  fetch  <slug> "<File:...>"    download, re-encode to 800px wide JPEG, to static/photos/<slug>.jpg and
                                print the front-matter lines (photo, photo_credit, photo_source)

Only licences that allow reuse with attribution are accepted (public domain, CC0, CC BY,
CC BY-SA). Anything else is refused at fetch time, not just hidden at search time.
"""
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://commons.wikimedia.org/w/api.php"
UA = "BeyondCertaintyPhotoBot/1.0 (https://beyondcertainty.ca; neonpulse314@gmail.com)"
SITE = Path(__file__).resolve().parent.parent
OK_LICENCE = re.compile(r"^(public domain|pd\b|pd-|cc0|cc by(-sa)? [0-9.]+|cc by(-sa)?$)", re.I)


def api(**params):
    params.update(format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def clean(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def info(titles, width=800):
    d = api(action="query", titles="|".join(titles), prop="imageinfo",
            iiprop="url|extmetadata|size|mime", iiurlwidth=width)
    out = []
    for p in d["query"]["pages"]:
        if "imageinfo" not in p:
            continue
        ii = p["imageinfo"][0]
        m = ii.get("extmetadata", {})
        out.append({
            "title": p["title"],
            "licence": clean(m.get("LicenseShortName", {}).get("value")),
            "artist": clean(m.get("Artist", {}).get("value")),
            "desc": clean(m.get("ImageDescription", {}).get("value"))[:140],
            "w": ii.get("width"), "h": ii.get("height"), "mime": ii.get("mime"),
            "thumb": ii.get("thumburl"), "page": ii.get("descriptionurl"),
            "licence_url": m.get("LicenseUrl", {}).get("value", ""),
        })
    return out


def search(q, n=8):
    d = api(action="query", list="search", srsearch=q + " filetype:bitmap",
            srnamespace=6, srlimit=n)
    titles = [h["title"] for h in d["query"]["search"]]
    if not titles:
        print("no results")
        return
    for c in info(titles):
        flag = "ok " if OK_LICENCE.match(c["licence"]) else "NO "
        print(f"{flag}{c['title']}\n    {c['licence']} | {c['artist'][:60]} | {c['w']}x{c['h']}\n    {c['desc']}")


def fetch(slug, title):
    c = info([title])
    if not c:
        sys.exit(f"not found: {title}")
    c = c[0]
    if not OK_LICENCE.match(c["licence"]):
        sys.exit(f"refused licence: {c['licence']!r}")
    # The summary licence is one field; the page's licence tags can disagree with it
    # (a "Public domain" summary on a page also tagged CC BY). Refuse a disagreement.
    cats = api(action="query", titles=title, prop="categories", cllimit="max")
    tags = {cl["title"].split(":", 1)[1].lower() for cl in cats["query"]["pages"][0].get("categories", [])}
    if c["licence"].lower().startswith("public domain") and any(t.startswith("cc-by") for t in tags):
        sys.exit(f"licence tags disagree (summary says public domain, page also has CC BY): read {c['page']}")
    dest = SITE / "static" / "photos" / f"{slug}.jpg"
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(c["thumb"], headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    from io import BytesIO
    from PIL import Image
    im = Image.open(BytesIO(data)).convert("RGB")
    im.thumbnail((800, 800 * 4))
    dest = dest.with_suffix(".jpg")
    im.save(dest, "JPEG", quality=78, optimize=True, progressive=True)
    data = dest.read_bytes()
    artist = c["artist"] or "Unknown author"
    credit = f"{artist}, {c['licence']}, via Wikimedia Commons"
    print(f"saved {dest.relative_to(SITE)} ({len(data)//1024} KB)")
    print(f'photo: "photos/{dest.name}"')
    print(f"photo_credit: {json.dumps(credit, ensure_ascii=False)}")
    print(f'photo_source: "{c["page"]}"')
    if c["licence_url"]:
        print(f'photo_licence_url: "{c["licence_url"]}"')


if __name__ == "__main__":
    if sys.argv[1] == "search":
        search(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 8)
    elif sys.argv[1] == "fetch":
        fetch(sys.argv[2], sys.argv[3])
