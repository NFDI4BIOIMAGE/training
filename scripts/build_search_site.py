from __future__ import annotations

import csv
import json
import shutil
from collections import Counter
from pathlib import Path

import yaml

FILTER_OUT_TAGS = ["include in DALIA", "exclude from DALIA"]
RECENT_ADDITIONS_COUNT = 10
TOP_DOWNLOADS_COUNT = 3


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [v for v in value if v not in (None, "")]
    return [value]


def _normalize_text(value):
    return " ".join(str(value).split()) if value is not None else ""


def _load_resources(path: Path):
    with path.open("r", encoding="utf-8") as stream:
        data = yaml.safe_load(stream) or {}

    # filter out the tags "include in DALIA" and "exclude from DALIA" as they are not relevant for the search site
    for resource in data.get("resources", []):
        tags = resource.get("tags", [])
        if isinstance(tags, list):
            resource["tags"] = [tag for tag in tags if tag not in FILTER_OUT_TAGS]

    return data.get("resources", [])


def _counter(resources, field):
    counter = Counter()
    for resource in resources:
        for item in _as_list(resource.get(field)):
            text = _normalize_text(item)
            if text:
                counter[text] += 1
    return counter


def _resource_search_text(resource):
    values = []
    for value in resource.values():
        if isinstance(value, list):
            values.extend(_normalize_text(v) for v in value)
        elif isinstance(value, dict):
            values.extend(_normalize_text(v) for v in value.values())
        else:
            values.append(_normalize_text(value))
    return " ".join(v for v in values if v)


def _json_safe(value):
    if isinstance(value, dict):
        return {k: _json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_json_safe(v) for v in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _top_downloads(download_dir: Path):
    snapshots = sorted(download_dir.glob("*.csv"))
    if len(snapshots) < 2:
        return []

    latest, previous = snapshots[-1], snapshots[-2]

    def read_rows(path: Path):
        rows = {}
        with path.open("r", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                url = row.get("url")
                if not url:
                    continue
                try:
                    downloads = int(float(row.get("downloads", 0)))
                except (TypeError, ValueError):
                    downloads = 0
                rows[url] = {"name": row.get("name", ""), "downloads": downloads}
        return rows

    latest_rows = read_rows(latest)
    previous_rows = read_rows(previous)

    ranked = []
    for url, data in latest_rows.items():
        delta = data["downloads"] - previous_rows.get(url, {}).get("downloads", 0)
        ranked.append(
            {
                "name": _normalize_text(data["name"]) or url,
                "url": url,
                "downloads": data["downloads"],
                "download_difference": delta,
            }
        )

    ranked.sort(key=lambda item: (item["download_difference"], item["downloads"]), reverse=True)
    return ranked[:TOP_DOWNLOADS_COUNT]


def build_site():
    repository_root = Path(__file__).resolve().parents[1]
    resources_path = repository_root / "resources" / "nfdi4bioimage.yml"
    download_dir = repository_root / "download_statistics"
    web_source = repository_root / "web"
    output_dir = repository_root / "dist"

    resources = _load_resources(resources_path)

    tags = _counter(resources, "tags")
    licenses = _counter(resources, "license")
    types = _counter(resources, "type")

    serializable_resources = []
    for resource in resources:
        normalized = _json_safe(resource)
        normalized["searchText"] = _resource_search_text(resource)
        serializable_resources.append(normalized)

    payload = {
        "totalResources": len(resources),
        "resources": serializable_resources,
        "mostCommonTags": [{"value": key, "count": value} for key, value in tags.most_common(1000)],
        "mostCommonLicenses": [{"value": key, "count": value} for key, value in licenses.most_common(1000)],
        "mostCommonTypes": [{"value": key, "count": value} for key, value in types.most_common(1000)],
        "recentAdditions": serializable_resources[-RECENT_ADDITIONS_COUNT:][::-1],
        "topDownloads": _top_downloads(download_dir),
    }

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    for static_file in ("index.html", "app.js", "styles.css", "server.py", "LinkedIn.png", "Mastodon.png", "Bluesky.png", "nfdi4bioimage-logo.png"):
        shutil.copy2(web_source / static_file, output_dir / static_file)

    shutil.copy2(repository_root / "docs" / "logo.png", output_dir / "logo.png")

    with (output_dir / "data.json").open("w", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False)


if __name__ == "__main__":
    build_site()
