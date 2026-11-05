#!/usr/bin/env python3
"""Build the sessions of this course from their content files with the LiaScript slide templates.

  python3 content/build.py                          build every content/*.txt and content/Selflearn/*.txt
  python3 content/build.py content/S04_X.txt ...    build only these files
  python3 content/build.py skeleton OUT.txt Template_A.md Template_B.md ...
                                                    new content file pre-filled with the guide examples

content/NAME.txt becomes NAME.md in the course folder, content/Selflearn/NAME.txt becomes Selflearn/NAME.md.
Templates are taken from templates/ (variants of this course) and from the template folder of the Tools
repository (environment variable LIA_TEMPLATES, default ~/GitHub/Teaching/Tools/2026/Templates via a relative path).
Lecture files get `classroom: enable` for the Edrys classrooms, self-study files are opened as a textbook.
"""
import os
import re
import sys
import tempfile
from pathlib import Path

CONTENT = Path(__file__).resolve().parent
COURSE = CONTENT.parent
TEMPLATES = Path(os.environ.get("LIA_TEMPLATES", COURSE.parents[3] / "Teaching" / "Tools" / "2026" / "Templates"))
LOCAL = COURSE / "templates"

sys.path.insert(0, str(TEMPLATES))
import assemble  # noqa: E402


def template_path(name):
    for folder in (LOCAL, TEMPLATES):
        if (folder / name).exists():
            return folder / name
    sys.exit(f"unknown template: {name}")


assemble.template_path = template_path

# Fixed English words of the general templates (instructions, alert titles, survey labels) in German.
# Only whole template phrases at the start of a line are replaced, never course content.
GERMAN = [
    (r"^> \[!NOTE\] Key message$", "> [!NOTE] Kernaussage"),
    (r"^> \[!NOTE\] Remember$", "> [!NOTE] Zum Merken"),
    (r"^> \[!NOTE\] Assessment$", "> [!NOTE] Prüfungsbezug"),
    (r"^> \[!TIP\] Why this matters$", "> [!TIP] Warum das wichtig ist"),
    (r"^> \[!WARNING\] Common misconception$", "> [!WARNING] Häufiges Missverständnis"),
    (r"^> \[!IMPORTANT\] Think about it until next time$", "> [!IMPORTANT] Zum Nachdenken bis zum nächsten Mal"),
    (r"^\*\*Order:\*\* Drag each card into the right gap\.$", "**Ordnen:** Ziehen Sie jede Karte in die richtige Lücke."),
    (r"\bStep (\d+): \[->\[", r"Schritt \1: [->["),
    (r"^\*\*Decide:\*\* True or false\?$", "**Entscheiden:** Richtig oder falsch?"),
    (r"^\*\*Decide:\*\* Which concept does each statement describe\?$",
     "**Entscheiden:** Welchen Begriff beschreibt die Aussage jeweils?"),
    (r"^\*\*Decide:\*\* ", "**Entscheiden:** "),
    (r"^\[\(true\) \(false\)\]$", "[(richtig) (falsch)]"),
    (r"^\[\(undecided\)\] Undecided$", "[(unentschieden)] Unentschieden"),
    (r"^\*\*Vote \(before\):\*\* ", "**Abstimmen (vorher):** "),
    (r"^\*\*Vote \(after\):\*\* ", "**Abstimmen (nachher):** "),
    (r"^\*\*Reflect:\*\* What is the most important thing you learned today – and what is still unclear\?$",
     "**Nachdenken:** Was ist das Wichtigste, das Sie gelernt haben – und was ist noch unklar?"),
    (r"^\*\*Reflect:\*\* ", "**Nachdenken:** "),
    (r"^\*\*Tick:\*\* What can you do now\?$", "**Abhaken:** Was können Sie jetzt?"),
    (r"^\*\*Feedback:\*\* How did this session work for you\?$", "**Feedback:** Wie hat diese Einheit für Sie funktioniert?"),
    (r"^\[\(1 agree\)\(2 rather agree\)\(3 neutral\)\(4 rather disagree\)\(5 disagree\)\]$",
     "[(1 stimme zu)(2 eher ja)(3 teils)(4 eher nein)(5 stimme nicht zu)]"),
    (r"^(\[\s+\]) The pace was appropriate\.$", r"\1 Das Tempo war angemessen."),
    (r"^(\[\s+\]) The explanations were clear\.$", r"\1 Die Erklärungen waren verständlich."),
    (r"^(\[\s+\]) The examples helped me understand\.$", r"\1 Die Beispiele haben mir beim Verstehen geholfen."),
    (r"^(\[\s+\]) The interactive parts were useful\.$", r"\1 Die Übungen waren nützlich."),
    (r"^\*\*(\d) · Choose one:\*\* ", r"**\1 · Eine Antwort:** "),
    (r"^\*\*(\d) · Choose all that apply:\*\* ", r"**\1 · Alle zutreffenden:** "),
    (r"^\*\*(\d) · Type:\*\* ", r"**\1 · Eintippen:** "),
    (r"^\*\*(\d) · Answer:\*\* ", r"**\1 · Ihre Antwort:** "),
    (r"^\*\*Type:\*\* ", "**Eintippen:** "),
    (r"^\*\*Complete:\*\*$", "**Ergänzen:**"),
    (r"^\*\*Mark:\*\* Which of these do you already know\? \(several possible\)$",
     "**Markieren:** Was davon kennen Sie schon? (mehrere möglich)"),
    (r"^\*\*By the end of this course you can …\*\*$", "**Am Ende dieser Einheit können Sie …**"),
    (r"^\*\*Choose:\*\* Which modules are you most curious about\? \(several possible\)$",
     "**Auswählen:** Auf welche Abschnitte sind Sie am meisten gespannt? (mehrere möglich)"),
    (r"^\| No \| Module \| Format \| Duration \|$", "| Nr. | Abschnitt | Format | Dauer |"),
    (r"^\| Know \| Can do \| Value \|$", "| Wissen | Können | Beurteilen |"),
    (r"^\| Criterion \|", "| Kriterium |"),
    (r"^\| Figure \| Value \|$", "| Angabe | Wert |"),
    (r"^\*\*Recap:\*\* ", "**Wiederholen:** "),
    (r"^\*\*➡️ Next:\*\* ", "**➡️ Als Nächstes:** "),
    (r"^<summary>✅ Model answer</summary>$", "<summary>✅ Musterantwort</summary>"),
    (r"^<summary>💡 Hint 1</summary>$", "<summary>💡 Hinweis</summary>"),
    (r"^<summary>✅ Solution</summary>$", "<summary>✅ Lösung</summary>"),
]


def germanize(text):
    for pattern, repl in GERMAN:
        text = re.sub(pattern, repl, text, flags=re.M)
    return text


AUTO_POOL = "@auto-exam-pool"


def exam_pool():
    """All questions of the Exam_Questions_Template_1 blocks in content/Selflearn/*.txt as one POOL line
    (entries 'unit|topic|question|where' separated by ' ;; ') for Random_Question_Template_1."""
    entries = []
    for path in sorted((CONTENT / "Selflearn").glob("*.txt")):
        unit = path.stem.split("_")[0] if re.match(r"S\d", path.stem) else "Prüfungstrainer"
        for name, values, _ in assemble.parse_content(path):
            if name != "Exam_Questions_Template_1.md":
                continue
            for n in range(1, 6):
                parts = [unit, values[f"Q{n}-TOPIC"], values[f"Q{n}"], f"{unit} – {values['SLIDE-TITLE']}"]
                parts = [re.sub(r'["`\\|]|;;', "", p).strip() for p in parts]
                entries.append("|".join(parts))
    return " ;; ".join(entries)


def build(content):
    rel = content.resolve().relative_to(CONTENT)
    out = COURSE / rel.with_suffix(".md")
    source = content.read_text(encoding="utf-8")
    if AUTO_POOL in source:
        with tempfile.NamedTemporaryFile("w", suffix=".txt", encoding="utf-8", delete=False) as tmp:
            tmp.write(source.replace(AUTO_POOL, exam_pool()))
        try:
            assemble.build(tmp.name, out)
        finally:
            os.unlink(tmp.name)
    else:
        assemble.build(content, out)
    text = out.read_text(encoding="utf-8")
    if rel.parent == Path("."):
        text = re.sub(r"^(mode:\s+Presentation)$", r"\1\nclassroom: enable", text, count=1, flags=re.M)
    else:
        text = re.sub(r"^mode:\s+Presentation$", "mode:     Textbook", text, count=1, flags=re.M)
        if re.search(r"^language:\s+de$", text, flags=re.M):
            text = germanize(text)
    out.write_text(text, encoding="utf-8")


def main():
    args = sys.argv[1:]
    if args[:1] == ["skeleton"] and len(args) >= 3:
        assemble.skeleton(args[1], args[2:])
        return
    files = [Path(a) for a in args] or sorted(CONTENT.glob("*.txt")) + sorted(CONTENT.glob("Selflearn/*.txt"))
    for content in files:
        build(content)


if __name__ == "__main__":
    main()
