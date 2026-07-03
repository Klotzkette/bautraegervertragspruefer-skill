# Bauträgervertrags-Akten zum Üben

Hier liegen zwei eigenständige, vollständig fingierte Bauträgervertrags-Akten. Sie sind als Gegensatzpaar gedacht: an der einen lässt sich zeigen, wie der Skill **unwirksame** Klauseln findet, an der anderen, wie er **wirksame, aber hart ausgereizte** Klauseln erkennt und sauber als verhandelbar statt als nichtig einordnet.

| Akte | Verzeichnis | Charakter | Erwartung an die Prüfung |
| --- | --- | --- | --- |
| Hohenwartshofen | [`bautraegervertrag/`](bautraegervertrag/) | bewusst fehlerhaft — überladen mit unwirksamen und teils nichtigen Klauseln | viele 🔴, klare Pflichtblock-Treffer |
| Marewald | [`bautraegervertrag-marewald/`](bautraegervertrag-marewald/) | rechtmäßig, aber grenzwertig verkäuferfreundlich — bis an die Grenze ausgereizt, ohne rote Pflichtverletzung | überwiegend 🟠, kein 🔴 wegen Nichtigkeit |

Jede Akte liegt in vier deutschen Formen vor: Markdown, Word und Gesamt-PDF sowie als **Akten-ZIP mit getrennten Einzel-PDFs** (Vertrag und Baubeschreibung separat), damit auch Modelle mit kleinem Kontext die Akte dokumentweise aufnehmen können. Zusätzlich gibt es zu beiden Verträgen eine deutsch-englische Lesefassung als HTML, Word und PDF: links die deutsche Urkundenfassung, rechts eine englische Verständnishilfe. In dieser Lesefassung ist ausdrücklich geregelt, dass bei der Beurkundung nur die deutsche Fassung verlesen wird und bei jedem Widerspruch ausschließlich die deutsche Fassung maßgeblich ist. Details und Download-Links stehen im README der jeweiligen Akte.

## So testet man den Skill damit

1. Skill laden: [`../skill/SKILL.md`](../skill/SKILL.md) (Vollfassung) oder [`../skill/MINI_SKILL.md`](../skill/MINI_SKILL.md) (kompakt).
2. Eine Akte als PDF, DOCX, Markdown oder als entpackte Einzel-PDFs übergeben.
3. Autonom prüfen lassen. Ergebnis ist immer ein Drei-Dokumente-Paket: Übersendungsschreiben an die Käuferseite, Mandantengutachten und außergerichtliches Aufforderungsschreiben an Bauträger/Notar.
4. Gegen die Erwartung in der Tabelle abgleichen: Findet der Skill bei Hohenwartshofen die roten Pflichtblock-Verstöße, und ordnet er Marewald als wirksam, aber ausgereizt ein, statt vorschnell Nichtigkeit zu behaupten?

## Wichtiger Hinweis

Beide Verträge sind keine Musterverträge. Parteien, Projekte und Aktenzeichen sind frei erfunden. Nicht unterschreiben, nicht als Vorlage verwenden, nicht in der Praxis einsetzen und nicht gegenüber echten Käufern, Bauträgern, Notariaten oder Behörden verwenden. Jede fachliche Bewertung setzt eine eigenständige rechtliche und technische Prüfung voraus.

## Selbst neu erzeugen

In jeder Akte erzeugt `./build.sh` aus der Markdown-Quelle die Word-Fassung, das Gesamt-PDF und das Akten-ZIP mit Einzel-PDFs. Die deutsch-englischen Lesefassungen werden repositoryweit mit `scripts/build_bilingual_contracts.py` erzeugt. Voraussetzungen: `pandoc`, `weasyprint`, `perl`, `zip`, `LibreOffice` und für eine vollständige Neuerzeugung der Lesefassung `argostranslate` mit Deutsch-Englisch-Modell.
