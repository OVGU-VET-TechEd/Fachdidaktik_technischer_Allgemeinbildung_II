# Sitzungen bauen

Die Sitzungen `S*.md` und `Selflearn/S*.md` werden aus den Inhaltsdateien in diesem Ordner erzeugt. Änderungen gehören in die `.txt`-Dateien, nicht in die `.md`-Dateien.

```bash
python3 content/build.py                                # alles neu bauen
python3 content/build.py content/S04_Bewertung_Fallstudie_Rollenspiel.txt   # eine Datei
python3 content/build.py skeleton OUT.txt Template1.md Template2.md          # leeres Inhaltsgerüst
```

- **Vorlagen:** zuerst `templates/` (Varianten dieses Kurses), dann die allgemeinen Vorlagen unter `Teaching/Tools/2026/Templates`. Ein anderer Pfad lässt sich mit der Umgebungsvariablen `LIA_TEMPLATES` setzen.
- **Vorlesung und Selbstlerneinheit:** `content/*.txt` wird im Modus Presentation mit `classroom: enable` gebaut, `content/Selflearn/*.txt` im Modus Textbook.
- **Weitere Prozess-Vorlagen:** `python3 make_process_templates.py 4 c5` im Ordner `templates/` erzeugt z. B. `Process_Template_4.md` und `Cycle_Template_5.md`.
- **Prüfen:** `validate.py` (Vorlagen) und `tools/render_check.mjs` (Darstellung im LiaScript-Viewer) liegen im allgemeinen Vorlagenordner.
- **Stolperstein:** Zwei HTML-Kommentare in aufeinanderfolgenden Zeilen zeigt LiaScript als Text an; dazwischen gehört eine Leerzeile.
- **Deutsche Beschriftung:** Die allgemeinen Vorlagen enthalten feste englische Wörter („Key message“, „Reflect:“, Umfrageskalen). `build.py` ersetzt sie in den Selbstlerneinheiten durch deutsche (Liste `GERMAN`); die Vorlesungsdateien bleiben unverändert.

## Prüfungsvorbereitung

- **Prüfungsfragen:** Jede Selbstlerneinheit endet mit `Exam_Questions_Template_1` – fünf Fragen mit aufklappbarer Antwortskizze (Begriff – Erläutern – Beispiel – Verbinden) und Selbsteinschätzung.
- **Prüfungstrainer:** `content/Selflearn/Pruefungstrainer.txt` → `Selflearn/Pruefungstrainer.md` – Fragen über alle Sitzungen, Querschnittsfragen, Fall und Prüfungssimulation. Die Simulation (`Random_Question_Template_1`) zieht zufällig aus allen Prüfungsfragen: `POOL = @auto-exam-pool` wird beim Bauen aus den `Exam_Questions_Template_1`-Blöcken aller Selbstlerneinheiten gefüllt. Nach Änderungen an Prüfungsfragen den Trainer neu bauen.

## SCORM-Pakete für Moodle

```bash
python3 content/export_scorm.py                                   # alle Selflearn/*.md
python3 content/export_scorm.py Selflearn/S03_Projektmethode.md   # eine Einheit
```

- SCORM 1.2, Markdown eingebettet (Moodle-4-Voreinstellung des LiaScript-Exporters), Bestehensgrenze 0 (nur Abschluss).
- Ausgabe: `Selflearn/SCORM/<Name>_SCORM.zip` (je ca. 7–8 MB) – der Ordner ist in `.gitignore`; die Pakete werden in Moodle hochgeladen.
- Mermaid-Diagramme und LiaScript-Vorlagen werden zur Laufzeit aus dem Internet geladen (GitHub, jsDelivr).
