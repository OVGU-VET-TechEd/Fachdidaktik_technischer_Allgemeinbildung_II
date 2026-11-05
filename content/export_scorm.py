#!/usr/bin/env python3
"""Export the self-study units as SCORM 1.2 packages for Moodle (elearning.ovgu.de).

  python3 content/export_scorm.py                              every Selflearn/*.md
  python3 content/export_scorm.py Selflearn/S03_Projektmethode.md ...   only these

Settings as for the first packages (S02, S06): SCORM 1.2 with the Markdown embedded in the package
(Moodle 4 preset of the LiaScript exporter), mastery score 0 (completion only, no pass mark).
Each unit is copied alone into a temporary folder, because the exporter packs the whole folder of the input.
Output: Selflearn/SCORM/<name>_SCORM.zip – the folder is git-ignored; upload the zips to Moodle.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

COURSE = Path(__file__).resolve().parent.parent
OUT = COURSE / "Selflearn" / "SCORM"
EXPORTER = "@liascript/exporter@3.4.2--2.1.0"
ORGANIZATION = "OVGU Magdeburg – Ingenieurpädagogik und Didaktik der technischen Bildung"
DURATION = {"S09_Medien_KI": "PT2H0M0S"}  # ISO 8601; default 90 minutes


def export(md):
    md = md.resolve()
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f"{md.stem}_SCORM"
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(md, Path(tmp) / md.name)
        cmd = ["npx", "-y", EXPORTER, "-i", str(Path(tmp) / md.name), "-f", "scorm1.2",
               "--scorm-embed", "--scorm-masteryScore", "0",
               "--scorm-organization", ORGANIZATION,
               "--scorm-typicalDuration", DURATION.get(md.stem, "PT1H30M0S"),
               "-o", str(target)]
        result = subprocess.run(cmd, capture_output=True, text=True)
    zip_path = target.with_suffix(".zip")
    if result.returncode or not zip_path.exists():
        sys.exit(f"export failed for {md.name}:\n{result.stdout[-2000:]}\n{result.stderr[-2000:]}")
    print(f"wrote {zip_path.relative_to(COURSE)} ({zip_path.stat().st_size / 1e6:.1f} MB)")


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted((COURSE / "Selflearn").glob("*.md"))
    for md in files:
        export(md)


if __name__ == "__main__":
    main()
