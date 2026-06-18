# Bauträgervertrag — grenzwertig, aber wirksam

Dieses Verzeichnis enthält einen zweiten, eigenständigen Übungsvertrag in drei Fassungen:

- [Markdown öffnen](bautraegervertrag-grenzwertig.md)
- [Word-Dokument herunterladen](bautraegervertrag-grenzwertig.docx)
- [PDF herunterladen](bautraegervertrag-grenzwertig.pdf)

Öffentliche Download-Links über GitHub Pages:

- [Markdown direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-grenzwertig/bautraegervertrag-grenzwertig.md)
- [Word-Dokument direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-grenzwertig/bautraegervertrag-grenzwertig.docx)
- [PDF direkt laden](https://klotzkette.github.io/bautraegervertragspruefer-skill/vertragsdokumente/bautraegervertrag-grenzwertig/bautraegervertrag-grenzwertig.pdf)

## Was dieser Vertrag soll

Anders als der erste Übungsvertrag (`../bautraegervertrag/`), der bewusst mit unwirksamen und nichtigen Klauseln überladen ist, ist dieser Vertrag das **wirksame Gegenstück**: Er reizt den verkäuferfreundlichen Spielraum bis an die Grenze des geltenden Rechts aus, bleibt dabei aber im Rahmen — keine Klausel ist erkennbar nichtig.

Konkret hält er die kritischen Pflichtpunkte ein und nutzt zugleich jede zulässige Härte zugunsten des Verkäufers:

- 5-%-Sicherheit nach § 650m Abs. 2 BGB wird gestellt (nicht abbedungen);
- MaBV-Fälligkeit nach § 3 Abs. 1 vollständig, sieben Teilbeträge, Schlussrate erst nach vollständiger Fertigstellung einschließlich Außenanlagen;
- anerkannte Regeln der Technik zum Zeitpunkt der Abnahme;
- fünf Jahre Mängelverjährung, gesetzliche Mängelrechte einschließlich Selbstvornahme;
- Abnahme des Gemeinschaftseigentums bleibt eigenes Recht jedes Erwerbers, keine bindende Fremdabnahme, keine Abnahmefiktion durch Dritte;
- Baubeschreibung als mitbeurkundete Bezugsurkunde mit konkreten Mindest-Kennwerten (z. B. Schallschutz R′w ≥ 54 dB / L′n,w ≤ 50 dB);
- Leistungsänderungen nur bei konkret benannten triftigen Gründen und gleichwertig;
- gebundene, aber wirksame Preis-, Frist- und Vollmachtsregelungen mit Lösungsrecht und Verbrauchergerichtsstand.

Erwartung an die Skill-Prüfung: viele 🟠-Verhandlungspunkte (Mindeststandards, harte Fristen-/Kosten-/Wartungsregeln, verkäuferfreundliche Auslegungsspielräume), aber im Ergebnis **kein 🔴 wegen Nichtigkeit** — der Skill soll diskutieren und sagen: hart, ausgereizt, nicht käuferfreundlich, aber wirksam.

## Wichtiger Hinweis

Dieser Bauträgervertrag ist kein Mustervertrag und darf nicht als Vorlage in der Praxis verwendet, nicht übernommen und nicht gegenüber echten Käuferinnen, Käufern, Bauträgern, Notariaten oder Behörden eingesetzt werden. Parteien, Projekt und Aktenzeichen sind frei erfunden. Für jede fachliche Bewertung ist eine eigenständige rechtliche und technische Prüfung erforderlich.

## Neu erzeugen

Nach Änderungen an `bautraegervertrag-grenzwertig.md` werden Word- und PDF-Fassung so erzeugt:

```bash
./build.sh
```

Voraussetzungen: `pandoc` und `weasyprint`. Layout und Seitenumbrüche steuern `build/style.css` und `build/pagebreak.lua`.
