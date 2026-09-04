#!/usr/bin/env python3
"""Rechenhilfe für § 3 Abs. 2 MaBV; keine Aussage zur rechtlichen Fälligkeit."""

import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

RESTSTUFEN = (
    ("Rohbau einschließlich Zimmererarbeiten", "40"), ("Dachflächen und Dachrinnen", "8"),
    ("Heizung Rohinstallation", "3"), ("Sanitär Rohinstallation", "3"),
    ("Elektro Rohinstallation", "3"), ("Fenster einschließlich Verglasung", "10"),
    ("Innenputz ohne Beiputz", "6"), ("Estrich", "3"), ("Sanitärfliesen", "4"),
    ("Bezugsfertigkeit gegen Besitzübergabe", "12"), ("Fassade", "3"),
    ("Vollständige Fertigstellung", "5"),
)


def zahl(text):
    # Deliberately reject thousands separators rather than guess what 1.234 means.
    try:
        value = Decimal(str(text).replace(",", "."))
    except InvalidOperation as error:
        raise ValueError("Zahl ohne Tausendertrennzeichen erforderlich") from error
    if not value.is_finite():
        raise ValueError("Endliche Zahl erforderlich")
    return value


def geld(value):
    return str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def berechnen(preis, erbbaurecht=False, gruppen=None, bezahlt="0", einbehalten="0"):
    preis, bezahlt, einbehalten = map(zahl, (preis, bezahlt, einbehalten))
    if preis <= 0 or min(bezahlt, einbehalten) < 0 or bezahlt + einbehalten > preis:
        raise ValueError("Kaufpreis positiv; Zahlung und Einbehalt nicht negativ und zusammen höchstens Kaufpreis")
    erste = Decimal("20" if erbbaurecht else "30")
    rest = Decimal(100) - erste
    stufen = [{"gewerk": "Beginn der Erdarbeiten", "gesamt_prozent": str(erste),
               "betrag_eur": geld(preis * erste / 100)}]
    for gewerk, quote in RESTSTUFEN:
        gesamt = rest * Decimal(quote) / 100
        stufen.append({"gewerk": gewerk, "rest_prozent": quote, "gesamt_prozent": str(gesamt),
                       "betrag_eur": geld(preis * gesamt / 100)})
    raten = []
    if gruppen is not None:
        quoten = [zahl(q) for q in gruppen]
        if not quoten or len(quoten) > 7 or min(quoten) <= 0 or sum(quoten) != 100:
            raise ValueError("Vertraglicher Gruppenplan: 1 bis 7 positive Gesamtquoten mit Summe genau 100 erforderlich")
        kumuliert = Decimal(0)
        vorher = Decimal(0)
        for nummer, quote in enumerate(quoten, 1):
            kumuliert += quote
            kumulativ = Decimal(geld(preis * kumuliert / 100))
            raten.append({"rate": nummer, "gesamt_prozent": str(quote),
                          "betrag_eur": geld(kumulativ - vorher),
                          "kumuliert_prozent": str(kumuliert), "kumuliert_eur": geld(kumulativ)})
            vorher = kumulativ
    sicherheit = preis * Decimal("0.05")
    return {
        "hinweis": "Rechenhilfe; weder Baufortschritt noch allgemeine Fälligkeitsvoraussetzungen, Gruppierungszulässigkeit oder Zahlbarkeit verifiziert.",
        "kaufpreis_eur": geld(preis), "erste_stufe_prozent": str(erste), "restbasis_prozent": str(rest),
        "mabv_stufen": stufen, "vertragliche_raten": raten,
        "sicherheit_fuenf_prozent_eur": geld(sicherheit),
        "bereits_einbehalten_eur": geld(einbehalten),
        "rechnerisch_noch_nicht_durch_einbehalt_gedeckt_eur": geld(max(Decimal(0), sicherheit - einbehalten)),
        "bereits_gezahlt_eur": geld(bezahlt),
        "offene_kaufpreissumme_eur": geld(preis - bezahlt),
        "rundung": "Gruppenbeträge aus Differenzen gerundeter kumulierter Beträge; vertragliche Cent-Rundung gesondert abgleichen.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preis", required=True, help="Euro ohne Tausendertrennzeichen")
    parser.add_argument("--erbbaurecht", action="store_true")
    parser.add_argument("--gruppen", help="Vertragliche Gesamtquoten, durch Semikolon getrennt")
    parser.add_argument("--bezahlt", default="0")
    parser.add_argument("--einbehalten", default="0")
    args = parser.parse_args()
    try:
        result = berechnen(args.preis, args.erbbaurecht, args.gruppen.split(";") if args.gruppen else None,
                           args.bezahlt, args.einbehalten)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
