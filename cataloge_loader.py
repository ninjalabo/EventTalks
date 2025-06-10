#!/usr/bin/env python3
"""
not working catalog_loader.py – build /mnt/data/no_auth_catalog.json
A resilient list of credential-free public APIs with downloadable OpenAPI specs.
Sources
  • APIs.guru directory         – 4 400+ APIs, CC-0 (live JSON) ¹
  • Public-APIs master list     – category feed, Auth=="No" ⁵  (fallback mirror ⁶)
If every network request fails we keep the previous catalogue, so the agent
never starts empty-handed.
"""
import asyncio, anyio, httpx, json, yaml, pathlib, re, sys
from datetime import datetime
from typing import List, Dict

OUT = pathlib.Path("no_auth_catalog.json")
OUT.parent.mkdir(parents=True, exist_ok=True)

# ── helpers ---------------------------------------------------------------
_SLUG = re.compile(r"[^a-zA-Z0-9_-]")
def slug(txt: str) -> str:
    txt = _SLUG.sub("_", txt).strip("_")
    return re.sub(r"__+", "_", txt)[:64] or "t"

async def safe_get(cx: httpx.AsyncClient, url: str) -> str | None:
    """GET text; on 404 auto-swap .yaml⇄.yml once.  Return None if still fails."""
    try:
        r = await cx.get(url, timeout=25); r.raise_for_status(); return r.text
    except (httpx.HTTPStatusError, httpx.ConnectError) as e:
        if isinstance(e, httpx.HTTPStatusError) and r.status_code == 404:
            if url.endswith(".yaml"):   # try .yml
                return await safe_get(cx, url[:-5] + ".yml")
            if url.endswith(".yml"):    # try .yaml
                return await safe_get(cx, url[:-4] + ".yaml")
        print(f"⚠ cannot GET {url} → {e}", file=sys.stderr)
        return None

# ── source 1: APIs.guru ---------------------------------------------------
async def fetch_guru(cx: httpx.AsyncClient) -> List[Dict]:
    root = "https://api.apis.guru/v2/list.json"
    idx_txt = await safe_get(cx, root)
    if idx_txt is None:
        return []
    idx = json.loads(idx_txt)
    rows = []
    for api_id, meta in idx.items():
        ver      = meta["versions"][meta["preferred"]]
        spec_url = ver.get("openapiUrl") or ver.get("swaggerUrl")
        if not spec_url:                # no spec file
            continue
        head = await safe_get(cx, spec_url)     # sniff securitySchemes
        if head is None:
            continue
        try:
            spec = json.loads(head)
        except json.JSONDecodeError:
            spec = yaml.safe_load(head)
        if spec.get("components", {}).get("securitySchemes"):
            continue                    # needs a key – skip
        rows.append(dict(
            id=slug(api_id),
            title=ver["info"]["title"],
            spec_url=spec_url,
            source="apis.guru"))
    return rows

# ── source 2: Public-APIs list (primary + mirror) -------------------------
PRIMARY  = "https://api.publicapis.org/entries"                     # often down ⁴
MIRROR   = ("https://raw.githubusercontent.com/public-api-lists/"
            "public-api-lists/main/collections/apis-no-auth.json")  # nightly feed ⁶

async def fetch_publicapis(cx: httpx.AsyncClient) -> List[Dict]:
    txt = await safe_get(cx, PRIMARY) or await safe_get(cx, MIRROR)
    if txt is None:
        print("⚠ Public-APIs feed unreachable – skipping", file=sys.stderr)
        return []
    feed = json.loads(txt)
    rows = []
    for row in feed.get("entries", []):
        if row.get("Auth", "").lower() != "no":
            continue
        if not row.get("OpenAPI"):      # no machine-readable spec link
            continue
        rows.append(dict(
            id=slug(row["API"]),
            title=row["API"],
            spec_url=row["OpenAPI"],
            source="public-apis"))
    return rows

# ── main builder ----------------------------------------------------------
async def build() -> None:
    async with httpx.AsyncClient(headers={"User-Agent": "catalog-builder/1.0"}) as cx:
        guru, pub = await asyncio.gather(fetch_guru(cx), fetch_publicapis(cx))

    uniq: Dict[str, Dict] = {row["spec_url"]: row for row in guru + pub}

    if not uniq:
        if OUT.exists():            # keep last good file
            print("⚠ All sources down; preserving existing catalogue", file=sys.stderr)
            return
        raise RuntimeError("All catalogue sources unreachable and no fallback file")

    OUT.write_text(json.dumps({
        "generated": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "count": len(uniq),
        "apis": list(uniq.values())},
        indent=2))
    print(f"✅ {len(uniq)} APIs saved → {OUT}")

if __name__ == "__main__":
    anyio.run(build)


