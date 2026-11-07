#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import shutil
import struct
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 95_000_000
SKIP_DIRS = {".git", "__pycache__", ".cursor"}

# Exact published tree after dropping API_DATA.json. CSVs here are aggregate
# tables, not raw API dumps. pipeline.tldraw.json is the diagram source.
ALLOWED_FILES = {
    ".gitignore",
    "AGENTS.md",
    "CHECK_PLAN.md",
    "README.md",
    "VERIFICATION.md",
    "demo.mp4",
    "docs/CONCEPT.md",
    "docs/REEL-DATA-BEAT.md",
    "docs/STRATEGY.md",
    "docs/charts/airbnb_listings_by_suburb.png",
    "docs/charts/camera_top10.png",
    "docs/charts/census_cars_and_solo.png",
    "docs/charts/food_drink_top.png",
    "docs/charts/hayfever_top.png",
    "docs/charts/hook_confidence.svg",
    "docs/charts/parking_gap.png",
    "docs/charts/parking_gap_recording.png",
    "docs/charts/singles_runclubs.png",
    "docs/charts/studio_vs_bedroom.png",
    "docs/charts/trees_top10.png",
    "docs/data/README.md",
    "docs/data/airbnb_by_suburb.csv",
    "docs/data/airbnb_vs_bond_1bed_postcode.csv",
    "docs/data/census_suburb_metrics.csv",
    "docs/data/events_angles_summary.csv",
    "docs/data/food_drink_by_suburb.csv",
    "docs/data/hayfever_by_suburb.csv",
    "docs/data/hook_review_summary.csv",
    "docs/data/parking_comparison.csv",
    "docs/data/runclub_catchment_prototype.csv",
    "docs/data/singles_suburbs.csv",
    "docs/data/studio_comparison.csv",
    "docs/hook-bank.md",
    "docs/pipeline.png",
    "docs/pipeline.tldraw.json",
    "docs/reel-report.html",
    "pitch.mp4",
    "report.html",
    "scripts/verify.py",
}
FORBIDDEN_PUBLISHED = re.compile(
    r"(API_DATA|\.env$|mb_raw|credential|\.pem$|\.key$)",
    re.I,
)

README_HEADINGS = ["What we built", "Data", "Status"]
README_PHRASES = [
    "PENDING",
    "human-led",
    "not built",
    "report.html",
    "docs/pipeline.png",
    "One Drop",
    "Botany",
    "not the subject of the existing",
]
AGENTS_REQUIRED = ["python3 scripts/verify.py", "--allow-pending", "python3 -m http.server"]
REPORT_HEADINGS = [
    "Data", "Method", "What worked", "What did not work", "Held-out check", "Limits", "Media",
]
REQUIRED_PHRASES = [
    "manual cross-endpoint definition check",
    "No independent audience or engagement validation yet",
    "PENDING",
    "PROVISIONAL",
    "failed independent cross-check",
    "omit the exact score",
    "fictional AI dramatisation",
    "withoutMicroburbs",
    "withMicroburbsAPI",
    "not a promised outcome",
]
NUMBER_SOURCES = {
    "0": "Microburbs: rescaled 0-100 score",
    "100": "Microburbs: rescaled 0-100 score",
    "94": "API /lifestyle/livability Surry Hills scores item key=lifestyle; PROVISIONAL",
    "91.0": "Public ranking page Surry Hills; unresolved vs 94",
    "1": "Task 1 name; API path /v1/",
    "6": "She Runs page: 6 km social run and 6:30am start",
    "30": "She Runs page: 6:30am start",
    "7": "Inspection / fetch date 7 Nov 2026",
    "2026": "Inspection / fetch date 7 Nov 2026",
    "15": "Task contract: demo 15-45 s",
    "45": "Task contract: demo 15-45 s, pitch <= 45 s",
    "1080": "Task contract: 1080x1920",
    "1920": "Task contract: 1080x1920",
    "95,000,000": "Hackathon guide: each video < 95,000,000 bytes",
    "3": "Peter: separate 3-minute walkthrough; official 3 pm close",
    "8000": "Local http.server port",
    "39.900": "ffprobe duration of reconstructed demo.mp4 (metadata only)",
}

EXPECTED_MEDIA = {
    "demo.mp4": {
        "sha256": "99d3ed08f48f101c7025e524efb3cb3bb3b0538759aa9ccc564795c2a5aca4c1",
        "size": 33815279,
        "duration": 39.9,
        "dur_lo": 15.0,
        "dur_hi": 45.0,
    },
    "pitch.mp4": {
        "sha256": "f322bb0ed0f0cc3abff56e5457c3f9010a64fa7294325712b507406ebb4af9a8",
        "size": 36459899,
        "duration": 45.0,
        "dur_lo": 0.0,
        "dur_hi": 45.0,
    },
}
PIPELINE_PNG_SHA256 = "f0b05abf6c797e6a0c2f80f9538ed657b6cc2d766c3aaef8ca55322c40c5e264"

SECRET_PATTERNS = {
    "openai_or_anthropic_key": re.compile(r"\bsk-[A-Za-z0-9_\-]{16,}"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    "google_api_key": re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}"),
    "slack_token": re.compile(r"\bxox[abpr]-[A-Za-z0-9\-]{10,}"),
    "bearer_token": re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}"),
    "key_assignment": re.compile(
        r"(api[_-]?key|token|secret|password|xi-api-key)\s*[:=]\s*['\"]?[A-Za-z0-9._\-]{12,}", re.I
    ),
}


class ReportParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self.links = []
        self.problems = []
        self.text = []
        self._in_heading = None
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("style", "script"):
            self._skip += 1
        if tag == "script":
            self.problems.append("contains <script>")
        if tag in ("h1", "h2", "h3"):
            self._in_heading = []
        for attr in ("src", "href", "poster", "srcset"):
            val = a.get(attr)
            if not val:
                continue
            remote = re.match(r"^(https?:)?//", val)
            if tag == "a" and attr == "href":
                if not remote and not val.startswith("#"):
                    self.links.append(val)
            elif remote:
                self.problems.append(f"remote asset <{tag} {attr}={val}>")
            else:
                self.links.append(val)

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self._skip -= 1
        if tag in ("h1", "h2", "h3") and self._in_heading is not None:
            self.headings.append("".join(self._in_heading).strip())
            self._in_heading = None

    def handle_data(self, data):
        if self._in_heading is not None:
            self._in_heading.append(data)
        if not self._skip:
            self.text.append(data)


class Result:
    def __init__(self):
        self.failures = []
        self.pending = []
        self.passes = []

    def check(self, ok, msg):
        (self.passes if ok else self.failures).append(msg)


def inventory():
    files = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        files.append(str(rel).replace("\\", "/"))
    return sorted(files)


def md_headings(text):
    return [m.group(1).strip() for m in re.finditer(r"^#{1,6}\s+(.+)$", text, re.M)]


def shipped_readme_section(text):
    marker = "# The shipped reel"
    idx = text.find(marker)
    return text[idx:] if idx >= 0 else text


def check_inventory(r, files):
    r.check("API_DATA.json" not in files, "inventory: API_DATA.json is not in the published tree")
    extra = [f for f in files if f not in ALLOWED_FILES]
    missing = sorted(ALLOWED_FILES - set(files))
    r.check(not extra, "inventory: no unexpected files"
            + (f" ({', '.join(extra)})" if extra else ""))
    r.check(not missing, "inventory: all allowlisted files present"
            + (f" (missing: {', '.join(missing)})" if missing else ""))
    for f in files:
        if FORBIDDEN_PUBLISHED.search(Path(f).name) or FORBIDDEN_PUBLISHED.search(f):
            r.check(False, f"inventory: forbidden published path {f}")
    r.check(True, f"inventory: {len(files)} files scanned against allowlist")


def check_markdown(r):
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    heads = md_headings(readme)
    for h in README_HEADINGS:
        r.check(any(h.lower() in x.lower() for x in heads), f"README heading: {h}")
    for p in README_PHRASES:
        r.check(p.lower() in readme.lower(), f"README phrase: {p}")
    for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", readme):
        alt, href = m.group(1).strip(), m.group(2).strip()
        r.check(len(alt) >= 40, "README pipeline image has meaningful alt text")
        r.check(not re.match(r"^(https?:)?//", href), f"README image is relative: {href}")
        exists = (ROOT / href).is_file()
        r.check(exists, f"README image resolves: {href}")
        if href.lower().endswith(".png") and exists:
            data = (ROOT / href).read_bytes()
            r.check(data[:8] == b"\x89PNG\r\n\x1a\n", f"README image is PNG: {href}")
            w, h = struct.unpack(">II", data[16:24])
            r.check(w >= 800 and h >= 800, f"README PNG dimensions {w}x{h}")
            digest = hashlib.sha256(data).hexdigest()
            r.check(digest == PIPELINE_PNG_SHA256, "README pipeline PNG sha256 unchanged")
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", readme):
        href = m.group(2).strip()
        if re.match(r"^(https?:)?//", href) or href.startswith("#") or href.startswith("mailto:"):
            continue
        r.check((ROOT / href).is_file(), f"README relative link resolves: {href}")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for c in AGENTS_REQUIRED:
        r.check(c in agents, f"AGENTS.md mentions: {c}")
    r.check((ROOT / "VERIFICATION.md").is_file(), "VERIFICATION.md exists")
    r.check((ROOT / "CHECK_PLAN.md").is_file(), "CHECK_PLAN.md exists")
    r.check("API_DATA.json" not in readme.lower() or "do not reintroduce" in readme.lower()
            or "drop `API_DATA.json`" in readme or "drop API_DATA.json" in readme,
            "README does not instruct keeping raw API_DATA.json in published history")
    return readme


def check_report(r):
    html = (ROOT / "docs/reel-report.html").read_text(encoding="utf-8")
    p = ReportParser()
    p.feed(html)
    for h in REPORT_HEADINGS:
        r.check(any(x.lower() == h.lower() for x in p.headings), f"report heading: {h}")
    for prob in p.problems:
        r.check(False, f"report: {prob}")
    r.check(not re.search(r"@import|url\(\s*['\"]?(https?:)?//", html, re.I),
            "report: no remote CSS imports/urls")
    text = " ".join(p.text)
    for ph in REQUIRED_PHRASES:
        r.check(ph.lower() in text.lower(), f"report phrase: {ph}")
    r.check("API_DATA.json" not in p.links, "report does not link to API_DATA.json")
    for link in p.links:
        if Path(link).name == "API_DATA.json":
            r.check(False, "report relative link to private API file")
            continue
        exists = (ROOT / "docs" / link).is_file() if not Path(link).is_absolute() else Path(link).is_file()
        # reel-report lives in docs/; relative links like ../demo.mp4
        target = (ROOT / "docs" / link).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            r.check(False, f"report link escapes repo: {link}")
            continue
        exists = target.is_file()
        if str(target.name).endswith(".mp4"):
            if exists:
                r.check(True, f"report relative media link present: {link}")
            else:
                r.pending.append(f"report links {link} (file absent)")
        else:
            r.check(exists, f"report relative link resolves: {link}")
    r.check((ROOT / "report.html").is_file(), "Suburb Secrets report.html present")
    return text


def check_wording(r, readme, report_text):
    blob = readme + "\n" + report_text
    r.check("94" in report_text and "91.0" in report_text,
            "wording: report keeps both 94 and 91.0")
    shipped = shipped_readme_section(readme)
    r.check("94" not in shipped and "91.0" not in shipped,
            "wording: shipped-reel README section does not headline the unresolved scores")
    r.check("report.html" in readme, "wording: README points to report.html for evidence")
    r.check("human-led" in readme.lower(), "wording: README says work is human-led today")
    r.check("onedropbrewingco.com.au/pages/whats-on" in readme.lower(),
            "wording: README One Drop official URL")
    r.check("she runs" in report_text.lower() and "st mary" in report_text.lower(),
            "wording: report keeps original She Runs video evidence")
    r.check("st mary" not in readme.lower() and "a.p. bakery" not in readme.lower(),
            "wording: README does not apply She Runs route to One Drop")
    r.check("not built" in readme.lower(), "wording: README marks calendar/feedback as not built")
    r.check("virality" in readme.lower() and ("not" in readme.lower() or "not guaranteed" in readme.lower()),
            "wording: README treats virality as a goal, not a guarantee")
    r.check("not a passed validation" in report_text.lower() or "unresolved, not validated" in report_text.lower(),
            "wording: contradictory score marked unresolved, not validated")
    r.check("working content engine" in readme.lower() and "not" in readme.lower(),
            "wording: no claim that a content engine exists")
    r.check("original music" in report_text.lower() and "jono" in report_text.lower(),
            "wording: report keeps original music and Jono narration")
    r.check("map" in report_text.lower() and "cathedral" in report_text.lower(),
            "wording: map instead of generated cathedral is documented")
    r.check("present" in blob.lower() and "pending" in blob.lower(),
            "wording: files PRESENT and final user approval PENDING")
    r.check("no disputed 94" in report_text.lower() or "omits the exact score" in report_text.lower()
            or "omit the exact score" in report_text.lower() or "omits the disputed 94" in report_text.lower(),
            "wording: videos omit disputed exact score")
    r.check("not visual/audio qa" in report_text.lower() or "not visual/audio QA" in report_text,
            "wording: ffprobe is not visual/audio QA")
    bad = []
    if re.search(r"\b94 is (the )?correct\b", blob, re.I):
        bad.append("94 treated as correct")
    if re.search(r"\b91\.0 is (the )?correct\b", blob, re.I):
        bad.append("91.0 treated as correct")
    if re.search(r"\b(we built|this (repo|repository) (is|has)|there is)\b.{0,40}\bautomatic content engine\b", blob, re.I):
        bad.append("automatic content engine claimed")
    r.check(not bad, "wording: no settled-score or engine overclaim"
            + (f" ({'; '.join(bad)})" if bad else ""))


def check_secrets(r, files):
    hits = []
    for f in files:
        path = ROOT / f
        if path.suffix.lower() in {".mp4", ".png", ".svg"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            hits.append(f"{f}: non-text file")
            continue
        for name, pat in SECRET_PATTERNS.items():
            n = len(pat.findall(text))
            if n:
                hits.append(f"{f}: {name} x{n}")
        if re.search(r'"endpoints"\s*:\s*\[', text) and "sample" in text and f != "scripts/verify.py":
            hits.append(f"{f}: looks like raw API dump")
        if path.name == "API_DATA.json":
            hits.append(f"{f}: raw API file present")
    for h in hits:
        r.check(False, f"credential/raw scan: {h}")
    r.check(True, "credential scan: completed on published files (values never printed)")


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error",
         "-show_entries", "stream=codec_name,codec_type,width,height:format=duration",
         "-of", "json", str(path)],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(out.stdout)
    video = next(s for s in data["streams"] if s.get("codec_type") == "video")
    audio = next(s for s in data["streams"] if s.get("codec_type") == "audio")
    return {
        "width": int(video["width"]),
        "height": int(video["height"]),
        "vcodec": video.get("codec_name"),
        "acodec": audio.get("codec_name"),
        "duration": float(data["format"]["duration"]),
    }


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def check_media(r, allow_pending):
    for name, spec in EXPECTED_MEDIA.items():
        path = ROOT / name
        if not path.is_file():
            msg = f"media: {name} missing"
            if allow_pending:
                r.pending.append(msg + " (PENDING approval)")
            else:
                r.check(False, msg)
            continue
        head = path.read_bytes()[:64]
        r.check(not head.startswith(b"version https://git-lfs.github.com"),
                f"media: {name} is a normal blob, not a Git LFS pointer")
        size = path.stat().st_size
        r.check(size < MAX_BYTES, f"media: {name} size {size} < {MAX_BYTES}")
        r.check(size == spec["size"], f"media: {name} size {size} == {spec['size']}")
        digest = sha256_file(path)
        r.check(digest == spec["sha256"], f"media: {name} sha256 matches producer handoff")
        if not shutil.which("ffprobe"):
            r.check(False, "media: ffprobe not found")
            continue
        try:
            info = probe(path)
        except (subprocess.CalledProcessError, KeyError, IndexError, ValueError, StopIteration) as e:
            r.check(False, f"media: ffprobe failed on {name}: {e}")
            continue
        r.check((info["width"], info["height"]) == (1080, 1920),
                f"media: {name} {info['width']}x{info['height']} == 1080x1920")
        r.check(info["vcodec"] == "h264", f"media: {name} video codec {info['vcodec']} == h264")
        r.check(info["acodec"] == "aac", f"media: {name} audio codec {info['acodec']} == aac")
        d = info["duration"]
        lo, hi = spec["dur_lo"], spec["dur_hi"]
        r.check(lo - 1e-3 <= d <= hi + 1e-3,
                f"media: {name} duration {d:.3f}s within {lo:g}-{hi:g}s")
        r.check(abs(d - spec["duration"]) <= 0.05,
                f"media: {name} duration {d:.3f}s matches handoff {spec['duration']:g}s")
        r.check(True, f"media: {name} ffprobe metadata only, not visual/audio QA")


def main():
    ap = argparse.ArgumentParser(description="Verify Task 1 docs and pending media.")
    ap.add_argument("--allow-pending", action="store_true",
                    help="docs-only mode: report missing videos as PENDING instead of failing")
    args = ap.parse_args()

    r = Result()
    files = inventory()
    check_inventory(r, files)
    readme = check_markdown(r)
    report_text = check_report(r)
    check_wording(r, readme, report_text)
    check_secrets(r, files)
    check_media(r, args.allow_pending)

    mode = "allow-pending (docs only)" if args.allow_pending else "strict"
    print(f"mode: {mode}")
    print("inventory:")
    for f in files:
        print(f"  {f}  {(ROOT / f).stat().st_size} bytes")
    for m in r.passes:
        print(f"PASS {m}")
    for m in r.pending:
        print(f"PENDING {m}")
    for m in r.failures:
        print(f"FAIL {m}")
    if r.failures:
        status = "FAIL"
    elif r.pending:
        status = "PASS (docs only; media PENDING, not submission-ready)"
    else:
        status = "PASS (strict; ffprobe metadata only, no visual/audio QA)"
    print(f"status: {status}")
    return 1 if r.failures else 0


if __name__ == "__main__":
    sys.exit(main())
