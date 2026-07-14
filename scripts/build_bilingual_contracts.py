#!/usr/bin/env python3
"""Build German/English two-column contract versions for the sample contracts.

The committed bilingual HTML files are generated artifacts, not separate legal
source documents. The German Markdown source remains authoritative.

Runtime dependency for translation generation:
  argostranslate with the German -> English package installed.

Rendering dependencies:
  pandoc, weasyprint, LibreOffice/soffice.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


try:
    import argostranslate.translate
except Exception:  # pragma: no cover - handled at runtime
    argostranslate = None


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ContractConfig:
    src: Path
    out_prefix: str
    short_title: str
    notary_de: str
    read_de: str
    deed_de: str


CONFIGS = [
    ContractConfig(
        src=ROOT / "vertragsdokumente/bautraegervertrag/bautraegervertrag.md",
        out_prefix="bautraegervertrag-de-en",
        short_title="Wohnungsbauträgervertrag mit Auflassung",
        notary_de="Der amtierende Notar",
        read_de="verliest",
        deed_de="beurkundet",
    ),
    ContractConfig(
        src=ROOT / "vertragsdokumente/bautraegervertrag-marewald/bautraegervertrag-marewald.md",
        out_prefix="bautraegervertrag-marewald-de-en",
        short_title="Wohnungsbauträgervertrag mit Auflassung",
        notary_de="Die amtierende Notarin",
        read_de="verliest",
        deed_de="beurkundet",
    ),
    ContractConfig(
        src=ROOT / "vertragsdokumente/bautraegervertrag-lindenhain/bautraegervertrag-lindenhain.md",
        out_prefix="bautraegervertrag-lindenhain-de-en",
        short_title="Wohnungsbauträgervertrag mit Auflassung",
        notary_de="Die amtierende Notarin",
        read_de="verliest",
        deed_de="beurkundet",
    ),
]


LANGUAGE_NOTICE = """## Sprachfassung, Verlesung und Verständnishilfe

**S.0** Diese Urkunde ist in einer deutsch-englischen Lesefassung erstellt. {notary_de} {deed_de} und {read_de} im Beurkundungstermin ausschließlich die deutsche Sprachfassung. Die englische Sprachfassung ist keine selbständige Vertragssprache, wird nicht verlesen und dient allein dem besseren Verständnis des Käufers; sie begründet keine von der deutschen Sprachfassung abweichenden Rechte, Pflichten, Fälligkeiten, Fristen, Beschaffenheiten oder Rechtsfolgen.
"""


LANGUAGE_NOTICE_EN = """## Language Version, Reading Aloud and Comprehension Aid

**S.0** This deed has been prepared as a German/English reading version. At the notarisation appointment, the acting notary records and reads aloud only the German language version. The English language version is not an independent contractual language, is not read aloud and serves solely to assist the Buyer in understanding the deed; it does not create any rights, obligations, due dates, time limits, qualities or legal consequences differing from the German language version.
"""


PRIORITY_CLAUSE_DE = """# Sprachvorrang

**SV.1** Bei Konflikten, Auslegungszweifeln, Abweichungen, Übersetzungsungenauigkeiten oder sonstigen Widersprüchen zwischen der deutschen und der englischen Sprachfassung ist ausschließlich die deutsche Sprachfassung maßgeblich. Die englische Sprachfassung tritt in jedem Fall hinter die deutsche Sprachfassung zurück und dient allein als Verständnishilfe.
"""


PRIORITY_CLAUSE_EN = """# Language Precedence

**SV.1** In the event of conflicts, doubts of interpretation, deviations, translation inaccuracies or any other inconsistencies between the German and English language versions, only the German language version shall be authoritative. The English language version shall in all cases be subordinate to the German language version and serves solely as a comprehension aid.
"""


EXACT_TRANSLATIONS = {
    "Verhandelt": "Recorded",
    "zu Berlin, am 14. März 2026": "in Berlin, on 14 March 2026",
    "zu Hamburg, am 12. Juni 2026": "in Hamburg, on 12 June 2026",
    "zu Köln, am 18. September 2026": "in Cologne, on 18 September 2026",
    "Vor mir, dem unterzeichnenden Notar im Bezirk des Kammergerichts": "Before me, the undersigned Notary in the district of the Kammergericht",
    "Vor mir, der unterzeichnenden Notarin im Bezirk des Hanseatischen Oberlandesgerichts": "Before me, the undersigned Notary in the district of the Hanseatic Higher Regional Court",
    "Vor mir, der unterzeichnenden Notarin im Bezirk des Oberlandesgerichts Köln": "Before me, the undersigned Notary in the district of the Higher Regional Court of Cologne",
    "erschienen heute:": "appeared today:",
    "dem Notar von Person bekannt,": "personally known to the Notary,",
    "der Notarin von Person bekannt,": "personally known to the Notary,",
    "ausgewiesen durch gültigen Personalausweis,": "identified by a valid identity card,",
    "Die Erschienenen baten sodann um die Beurkundung des nachstehenden": "The persons appearing then requested the notarisation of the following",
    "Die Erschienenen erklärten, dass sie auf das Verlesen der Bezugsurkunden verzichten, da ihnen deren Inhalt bekannt ist. Diese Niederschrift wurde den Erschienenen vom Notar vorgelesen, von ihnen genehmigt und sodann eigenhändig wie folgt unterschrieben:": "The persons appearing declared that they waived the reading aloud of the referenced deeds because they were familiar with their contents. This record was read aloud to the persons appearing by the Notary, approved by them and then signed by hand as follows:",
    "Diese Niederschrift nebst Anlage Baubeschreibung wurde den Erschienenen von der Notarin vorgelesen, von ihnen genehmigt und sodann eigenhändig unterschrieben:": "This record together with the annexed Building Specification was read aloud to the persons appearing by the Notary, approved by them and then signed by hand:",
    "Diese Niederschrift wurde den Erschienenen von der Notarin vorgelesen, von ihnen genehmigt und eigenhändig unterschrieben.": "This record was read aloud to the persons appearing by the Notary, approved by them and signed by hand.",
    "7.1 Die Besitzübergabe erfolgt nach Bezugsfertigkeit, Verkehrssicherheit der Zugänge und Zahlung oder berechtigtem Angebot der bis dahin fälligen Raten. Die Verkäuferin darf die Schlüssel nicht wegen streitiger, nicht fälliger oder berechtigt zurückbehaltener Beträge verweigern.": "7.1 Possession shall be transferred once the unit is ready for occupancy, safe access is available and the instalments due up to that point have been paid or duly tendered. The Seller may not withhold the keys on account of disputed amounts, amounts not yet due or amounts properly withheld.",
    "8.5 Die Gemeinschaft der Wohnungseigentümer übt nach § 9a Abs. 2 WEG die Rechte aus, die sich aus dem gemeinschaftlichen Eigentum ergeben, sowie solche Rechte der Erwerber, die eine einheitliche Rechtsverfolgung erfordern. Individuelle Abnahme- und Vorbehaltsrechte der Käuferin werden dadurch nicht ausgeschlossen.": "8.5 Pursuant to section 9a(2) WEG, the Community of Unit Owners exercises the rights arising from the Common Property and those purchasers' rights that require uniform enforcement. This does not exclude the Buyer's individual rights concerning acceptance or reservations of rights.",
    "9.4 Die Verkäuferin übergibt der Gemeinschaft die für Betrieb, Wartung und Verwaltung erforderliche geordnete Projektdokumentation spätestens mit Fertigstellung des jeweiligen gemeinschaftlichen Anlagenteils, keinesfalls später als bei dessen Besitzübergabe. Sie umfasst Wartungsverträge, Gewährleistungsübersicht, Prüfprotokolle, Revisionsunterlagen und Kontaktdaten der ausführenden Unternehmen; frühere Herausgabezeitpunkte nach § 5.2 bleiben unberührt.": "9.4 The Seller shall provide the Community of Unit Owners with the organised project documentation required for operation, maintenance and management no later than completion of the relevant part of the Common Property and in no event later than transfer of possession thereof. This includes maintenance agreements, a warranty schedule, inspection records, as-built documentation and contact details of the contractors; any earlier delivery dates under section 5.2 remain unaffected.",
    "8.5 Die Gemeinschaft der Wohnungseigentümer übt nach § 9a Abs. 2 WEG die sich aus dem gemeinschaftlichen Eigentum ergebenden Rechte sowie solche Rechte der Wohnungseigentümer aus, die eine einheitliche Rechtsverfolgung erfordern. Die individuellen Abnahme- und Vorbehaltsrechte der Käuferin werden dadurch nicht ausgeschlossen.": "8.5 Pursuant to section 9a(2) WEG, the Community of Unit Owners exercises the rights arising from the Common Property and those unit owners' rights that require uniform enforcement. This does not exclude the Buyer's individual rights concerning acceptance or reservations of rights.",
    "3.1 Kaufpreisraten werden erst fällig, wenn sämtliche allgemeinen Fälligkeitsvoraussetzungen des § 3 Abs. 1 MaBV vorliegen und die Notarin dies der Käuferin schriftlich bestätigt hat:": "3.1 Purchase Price instalments shall not become due until all general conditions set out in section 3(1) MaBV have been satisfied and the Notary has confirmed this to the Buyer in writing:",
    "wirksamer Vertrag, Vorliegen der für seinen Vollzug erforderlichen Genehmigungen und keine vertraglichen Rücktrittsrechte der Verkäuferin;": "a valid contract, all approvals required for its implementation and no remaining contractual right of the Seller to rescind;",
    "Eintragung einer Auflassungsvormerkung zugunsten der Käuferin an vereinbarter Rangstelle sowie Vollzug der Begründung des Wohnungseigentums;": "registration of a priority notice of conveyance in favour of the Buyer at the agreed rank and completion of the creation of the condominium ownership;",
    "gesicherte Freistellung von nicht zu übernehmenden vorrangigen oder gleichrangigen Grundpfandrechten auch bei nicht vollendetem Bauvorhaben und Aushändigung der hierfür erforderlichen Erklärungen an die Käuferin;": "secured release of prior-ranking or equal-ranking land charges that the Buyer is not to assume, including if the development is not completed, and delivery to the Buyer of the declarations required for that purpose;",
    "erteilte Baugenehmigung oder ein anderer Nachweis nach § 3 Abs. 1 Satz 1 Nr. 4 MaBV einschließlich der dort gegebenenfalls vorgeschriebenen Monatsfrist.": "the building permit or other evidence required by section 3(1), first sentence, no. 4 MaBV, including any one-month waiting period prescribed there.",
    "10.1 Zur Sicherung des Anspruchs der Käuferin auf Eigentumsverschaffung bewilligt und beantragt die Verkäuferin die Eintragung einer Auflassungsvormerkung im Grundbuch zugunsten der Käuferin.": "10.1 To secure the Buyer's claim to transfer of title, the Seller consents to and applies for registration of a priority notice of conveyance in favour of the Buyer in the Land Register.",
    "10.3 Die Verkäuferin verpflichtet sich, die Lastenfreistellung des Kaufgegenstands von der Globalgrundschuld zu bewirken, soweit diese nicht der Finanzierung der Käuferin dient. Die der Käuferin vor der ersten Rate auszuhändigende Freistellungserklärung muss gewährleisten, dass bei Vollendung des Bauvorhabens die nicht zu übernehmenden Grundpfandrechte unverzüglich nach Zahlung der geschuldeten Vertragssumme gelöscht werden. Für den Fall der Nichtvollendung muss sie die Löschung nach Zahlung des dem erreichten Bautenstand entsprechenden Vertragsteils oder die nach § 3 Abs. 1 Sätze 2 und 3 MaBV zulässige Rückzahlungslösung sichern.": "10.3 The Seller shall procure release of the Purchased Property from the global land charge to the extent that it does not secure the Buyer's financing. The release undertaking to be delivered to the Buyer before the first instalment must ensure that, if the development is completed, all land charges not to be assumed are deleted without delay after payment of the contract sum owed. If the development is not completed, it must secure deletion upon payment of the portion of the contract sum corresponding to the stage of construction reached or the repayment arrangement permitted by section 3(1), sentences 2 and 3 MaBV.",
    "10.4 Die Parteien sind über den Eigentumsübergang einig. Sie bewilligen und beantragen die Eigentumsumschreibung auf die Käuferin. Die Notarin wird angewiesen, die Eigentumsumschreibung erst zu beantragen, wenn der Kaufpreis fällig und gezahlt oder hinsichtlich streitiger Restbeträge berechtigt hinterlegt oder gesichert ist, die steuerliche Unbedenklichkeitsbescheinigung vorliegt und die Lastenfreistellung gesichert ist.": "10.4 The parties agree to the transfer of title and consent to and apply for registration of the Buyer as owner. The Notary is instructed not to apply for registration of title until the Purchase Price has become due and has been paid, or any disputed balance has properly been deposited or secured, the tax clearance certificate is available and release from encumbrances is secured.",
    "**7.2** Der Käufer trägt nur Beiträge und Kosten für nach Besitzübergabe neu beschlossene Maßnahmen, die weder der erstmaligen Erschließung noch der Erfüllung der Herstellungsverpflichtungen des Verkäufers dienen und nicht durch eine Pflichtverletzung des Verkäufers veranlasst sind.": "**7.2** The Buyer shall bear only contributions and costs relating to measures newly resolved after transfer of possession which neither serve the initial development of the property nor discharge the Seller's construction obligations and which were not occasioned by a breach of duty by the Seller.",
}


MANUAL_TRANSLATIONS = {
    LANGUAGE_NOTICE.format(
        notary_de="Der amtierende Notar", deed_de="beurkundet", read_de="verliest"
    )
    .strip()
    .split("\n\n", 1)[1]: LANGUAGE_NOTICE_EN.strip().split("\n\n", 1)[1],
    LANGUAGE_NOTICE.format(
        notary_de="Die amtierende Notarin", deed_de="beurkundet", read_de="verliest"
    )
    .strip()
    .split("\n\n", 1)[1]: LANGUAGE_NOTICE_EN.strip().split("\n\n", 1)[1],
    PRIORITY_CLAUSE_DE.strip().split("\n\n", 1)[1]: PRIORITY_CLAUSE_EN.strip().split("\n\n", 1)[1],
}


def translate(text: str) -> str:
    if not text.strip():
        return text
    if argostranslate is None:
        raise RuntimeError(
            "argostranslate is not available. Install argostranslate and the de->en package."
        )
    result = argostranslate.translate.translate(text, "de", "en")
    return polish_translation(result)


def polish_translation(text: str) -> str:
    text = re.sub(r"\*\*([^*\n]*?)\s+\*\*", r"**\1**", text)
    replacements = {
        "seller": "Seller",
        "buyer": "Buyer",
        "notary": "Notary",
        "purchase price": "Purchase Price",
        "purchase item": "Purchased Property",
        "object of purchase": "Purchased Property",
        "contract object": "Purchased Property",
        "building description": "Building Specification",
        "division declaration": "Declaration of Division",
        "land register": "Land Register",
        "special property": "Unit Property",
        "Sondereigentum": "Unit Property",
        "common property": "Common Property",
        "joint ownership": "Common Property",
        "community of apartment owners": "Community of Unit Owners",
        "joint property": "Common Property",
        "provision for disposition": "priority notice of conveyance",
        "disposition reservation": "priority notice of conveyance",
        "property reserve": "priority notice of conveyance",
        "property reservation": "priority notice of conveyance",
        "reservation train by train": "priority notice of conveyance concurrently",
        "Global Grundschuld": "global land charge",
        "global basic liability": "global land charge",
        "basic liability": "land charge",
        "basic debt": "land charge",
        "basic financing liens": "financing land charges",
        "object monitoring": "site supervision",
        "construction description": "Building Specification",
        "description of the building": "Building Specification",
        "construction target": "contractual construction specification",
        "contractual production": "contractual construction",
        "production obligation": "construction obligation",
        "production obligations": "construction obligations",
        "complete production": "complete construction",
        "timely production": "timely construction",
        "defect-free production": "defect-free construction",
        "production scope": "construction scope",
        "ready-to-cover production": "readiness for occupancy",
        "subscription readiness": "readiness for occupancy",
        "subscription skill": "readiness for occupancy",
        "reference skill": "readiness for occupancy",
        "ready to move": "ready for occupancy",
        "ground exploitation and connection costs": "development and connection costs",
        "recognized rules of the technique": "recognised rules of technology",
        "recognized rules of technology": "recognised rules of technology",
        "rules of technology": "rules of technology",
        "MK-Bound": "MK-Boden",
        "Flash or special fittings": "Flush or special fittings",
        "multiplelocking": "multiple locking",
        "Makler- und Bauträgerverordnung": "German Makler- und Bauträgerverordnung (MaBV)",
        "Published today:": "appeared today:",
        "Business resident:": "business address:",
        "resident:": "resident at:",
        "issued by a valid identity card": "identified by a valid identity card",
        "known to the Notary by person": "personally known to the Notary",
        "WAY": "WEG",
        "insolvency reserve": "priority notice of conveyance",
        "property acquisition": "acquisition of title",
        "owners of the dwelling": "unit owners",
        "apartment ownership": "condominium ownership",
        "maturity requirements": "conditions for payment to become due",
        "form-needed": "subject to mandatory form requirements",
        "publications": "persons appearing",
        "publication": "person appearing",
        "Declaration of partition": "Declaration of Division",
        "Community order": "Community Rules",
        "community order": "Community Rules",
        "sample line": "selection range",
        "sample series": "selection series",
        "sample documentation": "selection documentation",
        "dismissal reservation": "priority notice of conveyance",
        "burden exemption": "release from encumbrances",
        "load exemption": "release from encumbrances",
    }
    for old, new in replacements.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    phrase_replacements = {
        "** at the time": " at the time",
        "**and* payments": "and payments",
        "The Seller authorizes and authorizes": "The Seller authorizes",
        "The Seller hereby authorizes and authorizes": "The Seller hereby authorizes",
        "the registration of a priority notice of conveyance train by train": "the deletion of a priority notice of conveyance concurrently",
        "the deletion of the priority notice of conveyance train by train": "the deletion of the priority notice of conveyance concurrently",
        "the property reservation train by train": "the priority notice of conveyance concurrently",
        "statement of insolvency in accordance with § 883 BGB": "priority notice of conveyance pursuant to § 883 BGB",
        "dismissal only after receipt": "registration only after receipt",
        "the Purchased Property in the position": "the Purchased Property in its position",
        "if the Seller asks": "when the Seller asks",
        "Seller asks the Buyer in writing to pay": "Seller requests payment from the Buyer in writing",
        "Skill of reference and train by train against transfer of ownership": "Readiness for occupancy concurrently with transfer of possession",
        "skill of reference": "readiness for occupancy",
        "train by train": "concurrently",
        "The transfer of ownership takes place according to the readiness for occupancy": "Possession shall be transferred once the unit is ready for occupancy",
        "Economic transfer of ownership": "Transfer of possession",
        "Transfer of ownership, Acceptance": "Transfer of Possession and Acceptance",
        "transfer of ownership, acceptance": "transfer of possession and acceptance",
        "after the transfer of ownership": "after transfer of possession",
        "after transfer of ownership": "after transfer of possession",
        "upon transfer of ownership of unit B-05": "upon transfer of possession of unit B-05",
        "upon transfer of ownership": "upon transfer of possession",
        "consultation hours in the sample": "consultation hours during the selection appointment",
        "framework of a sample": "selection process",
        "specified in the sample": "specified during selection",
        "sample from these series": "selection from these series",
        "Safeguarding of property, reservation, release of burdens, dissolution": "Protection of Title, Priority Notice of Conveyance, Release from Encumbrances and Conveyance",
        "the disposition": "the conveyance",
        "disposition only after": "conveyance for registration only after",
        "A deletion of the reservation": "Deletion of the priority notice of conveyance",
        "deletion of the reservation": "deletion of the priority notice of conveyance",
        "the reservation and delivers it": "the consent to deletion of the priority notice of conveyance and delivers it",
        "Competence requires": "Readiness for occupancy requires",
        "free of loads": "free from encumbrances",
        "exemption from loads": "release from encumbrances",
        "unaccepted loads": "encumbrances not assumed",
        "load release": "release from encumbrances",
        "global mortgage": "global land charge",
        "declaration of exemption": "release undertaking",
        "Broker and Builders Ordinance": "German Makler- und Bauträgerverordnung",
        "Broker and property development regulation": "German Makler- und Bauträgerverordnung",
        "MABV": "MaBV",
        "apply for the property transfer": "apply for registration of title",
        "transfer of property only when": "registration of title only when",
        "You approve and apply": "They consent to and apply",
        "Readiness to reference Train to train against transfer of ownership": "Readiness for occupancy concurrently with transfer of possession",
        "shows the readiness for occupancy and invites to a joint walk": "gives notice of readiness for occupancy and invites the Buyer to a joint inspection",
        "Acquisition of the special ownership unit": "Acceptance of the Unit Property",
        "Declaration of reference 1": "Referenced Deed 1",
        "reference documents": "referenced deeds",
        "load-free property transfer": "registration of title free from encumbrances",
        "property transfer": "registration of title",
        "transfer of property": "registration of title",
    }
    for old, new in phrase_replacements.items():
        text = text.replace(old, new)
    text = text.replace("**", "")
    text = text.replace("§ §", "§§")
    text = text.replace("EUR", "EUR")
    return text


def split_blocks(markdown: str) -> list[str]:
    lines = markdown.splitlines()
    blocks: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.strip() == r"\newpage":
            blocks.append(r"\newpage")
            i += 1
            continue
        if line.lstrip().startswith("#"):
            blocks.append(line)
            i += 1
            continue
        if line.startswith("|"):
            table = [line]
            i += 1
            while i < len(lines) and lines[i].startswith("|"):
                table.append(lines[i])
                i += 1
            blocks.append("\n".join(table))
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items = [line]
            i += 1
            while i < len(lines) and (not lines[i].strip() or re.match(r"^\s*[-*]\s+", lines[i])):
                if lines[i].strip():
                    items.append(lines[i])
                i += 1
            blocks.append("\n".join(items))
            continue

        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if not nxt.strip():
                break
            if nxt.strip() == r"\newpage" or nxt.lstrip().startswith("#") or nxt.startswith("|") or re.match(r"^\s*[-*]\s+", nxt):
                break
            para.append(nxt)
            i += 1
        blocks.append("\n".join(para))
    return blocks


def inject_language_notice(blocks: list[str], cfg: ContractConfig) -> list[str]:
    notice_de = LANGUAGE_NOTICE.format(
        notary_de=cfg.notary_de, deed_de=cfg.deed_de, read_de=cfg.read_de
    ).strip()
    result: list[str] = []
    inserted = False
    for index, block in enumerate(blocks):
        result.append(block)
        if not inserted and index == 0 and block.startswith("# "):
            result.extend(split_blocks(notice_de))
            inserted = True
    if not inserted:
        result[0:0] = split_blocks(notice_de)
    result.extend([r"\newpage", *split_blocks(PRIORITY_CLAUSE_DE.strip())])
    return result


def translate_block(block: str) -> str:
    if block == r"\newpage":
        return block
    if block in MANUAL_TRANSLATIONS:
        return MANUAL_TRANSLATIONS[block]
    if block.startswith("#"):
        prefix, title = re.match(r"^(#+)\s+(.*)$", block).groups()  # type: ignore[union-attr]
        manual = {
            "Bauträgervertrag": "Property Development Contract",
            "Wohnungsbauträgervertrag mit Auflassung": "Residential Property Development Contract with Conveyance",
            "Sprachfassung, Verlesung und Verständnishilfe": "Language Version, Reading Aloud and Comprehension Aid",
            "Sprachvorrang": "Language Precedence",
            "Anlage: Baubeschreibung": "Annex: Building Specification",
            "Schlussbestimmungen der Baubeschreibung": "Final Provisions of the Building Specification",
            "§ 6 Besitzübergang, Abnahme": "§ 6 Transfer of Possession and Acceptance",
            "7 Besitzübergabe, Abnahme": "7 Transfer of Possession and Acceptance",
            "§ 5 Wirtschaftlicher Besitzübergang, Abnahme, Schlüsselübergabe": "§ 5 Transfer of Possession, Acceptance and Handover of Keys",
            "10 Eigentumssicherung, Vormerkung, Lastenfreistellung, Auflassung": "10 Protection of Title, Priority Notice of Conveyance, Release from Encumbrances and Conveyance",
            "9 Bemusterung, Auswahlrechte": "9 Selection of Finishes and Selection Rights",
            "14 Wohnfläche, Bemusterung": "14 Residential Floor Area and Selection of Finishes",
        }
        return f"{prefix} {manual.get(title, translate(title))}"
    if block.startswith("|"):
        return translate_markdown_table(block)
    if re.match(r"^\s*[-*]\s+", block):
        out = []
        for line in block.splitlines():
            marker, rest = re.match(r"^(\s*[-*]\s+)(.*)$", line).groups()  # type: ignore[union-attr]
            out.append(marker + translate_clause_text(rest))
        return "\n".join(out)
    return translate_clause_text(block)


def translate_clause_text(text: str) -> str:
    if text in EXACT_TRANSLATIONS:
        return EXACT_TRANSLATIONS[text]
    if re.fullmatch(r"\*\*[^*\n]+\*\*", text.strip()):
        return text
    for prefix_de, prefix_en in [
        ("geschäftsansässig:", "business address:"),
        ("Geschäftsanschrift:", "business address:"),
        ("wohnhaft:", "resident at:"),
    ]:
        if text.startswith(prefix_de):
            return prefix_en + text[len(prefix_de) :]
    leading = re.match(r"^(\*\*[A-Za-z0-9.]+\*\*\s*)(.*)$", text, flags=re.S)
    if leading:
        return leading.group(1) + translate(leading.group(2))
    if text.strip() in {"\\", "——————————————————————————"}:
        return text
    if re.fullmatch(r"[\s\\—–-]+", text.strip()):
        return text
    return translate(text)


def split_table_row(row: str) -> list[str]:
    inner = row.strip().strip("|")
    return [cell.strip() for cell in inner.split("|")]


def translate_markdown_table(block: str) -> str:
    rows = block.splitlines()
    translated = []
    for idx, row in enumerate(rows):
        cells = split_table_row(row)
        if idx == 1 and all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            translated.append(row)
            continue
        translated_cells = []
        for cell in cells:
            if re.fullmatch(r"[:\-\s]+", cell) or re.fullmatch(
                r"(?:EUR\s*)?[0-9.,+\-/%€\s]+", cell
            ):
                translated_cells.append(cell)
            else:
                translated_cells.append(translate(cell))
        translated.append("| " + " | ".join(translated_cells) + " |")
    return "\n".join(translated)


def markdown_to_html(block: str) -> str:
    if block == r"\newpage":
        return ""
    if not block.strip():
        return ""
    proc = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html"],
        input=block,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout.strip()


def bilingual_rows(blocks: list[str], english_blocks: list[str]) -> str:
    rows = [
        '<table class="bilingual-table">',
        "<colgroup><col><col></colgroup>",
        "<thead><tr><th>Deutsche Fassung</th><th>English convenience translation</th></tr></thead>",
        "<tbody>",
    ]
    for de, en in zip(blocks, english_blocks):
        if de == r"\newpage":
            rows.append('<tr class="pagebreak"><td colspan="2"></td></tr>')
            continue
        de_html = markdown_to_html(de)
        en_html = markdown_to_html(en)
        rows.append(
            "<tr>"
            f'<td class="de">{de_html}</td>'
            f'<td class="en">{en_html}</td>'
            "</tr>"
        )
    rows.append("</tbody></table>")
    return "\n".join(rows)


def html_document(title: str, body: str, source_sha256: str) -> str:
    escaped_title = html.escape(title)
    provenance = f"btv-source-sha256:{source_sha256}"
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="description" content="{provenance}">
<meta name="keywords" content="{provenance}">
<meta name="btv-source-sha256" content="{source_sha256}">
<title>{escaped_title}</title>
<style>
@page {{
  size: A4 landscape;
  margin: 1.35cm 1.15cm 1.25cm 1.15cm;
  @bottom-center {{
    content: counter(page);
    font-family: "DejaVu Serif", Georgia, serif;
    font-size: 8pt;
    color: #666;
  }}
}}
body {{
  font-family: "DejaVu Serif", Georgia, serif;
  color: #111;
  font-size: 8.4pt;
  line-height: 1.34;
}}
.doc-title {{
  font-size: 16pt;
  margin: 0 0 0.8em;
  letter-spacing: 0;
}}
.doc-note {{
  margin: 0 0 1em;
  color: #333;
  font-size: 8.6pt;
}}
table.bilingual-table {{
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}}
.bilingual-table > colgroup > col {{ width: 50%; }}
.bilingual-table > thead th {{
  border: 0.8px solid #555;
  background: #eeeeee;
  padding: 5px 7px;
  text-align: left;
  font-weight: bold;
  font-size: 8.8pt;
}}
.bilingual-table > tbody > tr > td {{
  border: 0.45px solid #b5b5b5;
  vertical-align: top;
  padding: 5px 7px;
}}
.bilingual-table tr.pagebreak td {{
  border: none;
  padding: 0;
  height: 0;
  page-break-after: always;
}}
h1 {{
  font-size: 11.4pt;
  margin: 0.3em 0 0.35em;
  padding-bottom: 1px;
  border-bottom: 0.8px solid #333;
  page-break-after: avoid;
}}
h2 {{
  font-size: 9.8pt;
  margin: 0.45em 0 0.25em;
  page-break-after: avoid;
}}
h3 {{
  font-size: 9pt;
  margin: 0.4em 0 0.2em;
  page-break-after: avoid;
}}
p {{ margin: 0.35em 0; }}
blockquote {{
  margin: 0.35em 0 0.35em 0.25em;
  padding: 0.05em 0 0.05em 0.55em;
  border-left: 1.5px solid #aaa;
}}
td table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 7.6pt;
  margin: 0.35em 0;
}}
td table th, td table td {{
  border: 0.35px solid #999;
  padding: 2px 3px;
  vertical-align: top;
  text-align: left;
}}
td table th {{ background: #f0f0f0; }}
ul, ol {{ margin: 0.3em 0 0.3em 1.15em; padding: 0; }}
li {{ margin: 0.2em 0; }}
strong {{ font-weight: bold; }}
</style>
</head>
<body>
<h1 class="doc-title">{escaped_title}</h1>
<p class="doc-note">Deutsch-englische Lesefassung. Bei Abweichungen ist die deutsche Sprachfassung maßgeblich.</p>
{body}
</body>
</html>
"""


WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def repair_bilingual_docx_tables(path: Path) -> None:
    """Flatten nested rate tables that LibreOffice misplaces during HTML import.

    LibreOffice keeps the surrounding German/English table intact for prose, but
    imports the two nested Markdown tables into swapped cells at excessive width.
    Converting each rate row to a compact paragraph preserves the two-column
    reading order and prevents clipping in Word and LibreOffice.
    """

    qn = lambda name: f"{{{WORD_NS}}}{name}"
    ET.register_namespace("w", WORD_NS)

    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))

    parents = {child: parent for parent in root.iter() for child in parent}

    def ancestor(element: ET.Element, tag: str) -> ET.Element | None:
        parent = parents.get(element)
        while parent is not None and parent.tag != qn(tag):
            parent = parents.get(parent)
        return parent

    def element_text(element: ET.Element) -> str:
        return "".join(node.text or "" for node in element.iter(qn("t")))

    english_rate_replacements = {
        "Stichmonat": "Construction milestone",
        "Bautenstand": "Construction status",
        "Anteil": "Percentage",
        "Betrag": "Percentage",
        "nach Beginn der Erdarbeiten": "after commencement of earthworks",
        "Beginn der Erdarbeiten, nach Vorliegen der Voraussetzungen aus § 3.1": (
            "after commencement of earthworks and satisfaction of the conditions in § 3.1"
        ),
        "nach Fassadenarbeiten": "after completion of facade works",
        "Innenputz, Estrich und Fassadenarbeiten": (
            "interior plaster, screed and facade works"
        ),
        "Readiness to reference Train to train against transfer of ownership": (
            "readiness for occupancy concurrently with transfer of possession"
        ),
        "Readiness to reference train to train against transfer of ownership": (
            "readiness for occupancy concurrently with transfer of possession"
        ),
        "Skill of reference and train by train against transfer of ownership": (
            "readiness for occupancy concurrently with transfer of possession"
        ),
    }

    def table_lines(table: ET.Element, *, english: bool) -> list[ET.Element]:
        paragraphs: list[ET.Element] = []
        for index, row in enumerate(table.findall(qn("tr"))):
            values = [element_text(cell).strip() for cell in row.findall(qn("tc"))]
            if english:
                values = [english_rate_replacements.get(value, value) for value in values]
            paragraph = ET.Element(qn("p"))
            properties = ET.SubElement(paragraph, qn("pPr"))
            ET.SubElement(
                properties,
                qn("pStyle"),
                {qn("val"): "TableHeading" if index == 0 else "TableContents"},
            )
            ET.SubElement(properties, qn("spacing"), {qn("before"): "0", qn("after"): "80"})
            run = ET.SubElement(paragraph, qn("r"))
            if index == 0:
                run_properties = ET.SubElement(run, qn("rPr"))
                ET.SubElement(run_properties, qn("b"))
            text = ET.SubElement(run, qn("t"))
            text.text = " · ".join(values)
            paragraphs.append(paragraph)
        return paragraphs

    tables = list(root.iter(qn("tbl")))
    if not any(list(table.iter(qn("tbl")))[1:] for table in tables):
        return
    innermost_tables = [
        table for table in tables if not list(table.iter(qn("tbl")))[1:]
    ]
    if not innermost_tables:
        return
    if len(innermost_tables) % 2:
        raise RuntimeError(f"Unexpected nested table count in {path}: {len(innermost_tables)}")

    for german_table, english_table in zip(innermost_tables[::2], innermost_tables[1::2]):
        german_cell = ancestor(german_table, "tc")
        english_cell = ancestor(english_table, "tc")
        german_row = ancestor(german_cell, "tr") if german_cell is not None else None
        english_row = ancestor(english_cell, "tr") if english_cell is not None else None
        outer_table = ancestor(german_row, "tbl") if german_row is not None else None
        if any(
            element is None
            for element in (german_cell, english_cell, german_row, english_row, outer_table)
        ):
            raise RuntimeError(f"Could not locate bilingual table structure in {path}")
        if outer_table is not ancestor(english_row, "tbl"):
            raise RuntimeError(f"Nested tables do not share an outer table in {path}")

        target_cells = german_row.findall(qn("tc"))
        english_cells = english_row.findall(qn("tc"))
        if len(target_cells) != 2 or not english_cells:
            raise RuntimeError(f"Unexpected bilingual row geometry in {path}")
        if german_cell is not target_cells[1] or english_cell is not english_cells[0]:
            raise RuntimeError(f"LibreOffice table import shape changed in {path}")

        german_lines = table_lines(german_table, english=False)
        english_lines = table_lines(english_table, english=True)
        german_cell.remove(german_table)
        english_cell.remove(english_table)
        for paragraph in german_lines:
            target_cells[0].append(paragraph)
        for paragraph in english_lines:
            target_cells[1].append(paragraph)
        outer_table.remove(english_row)

    document_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    temporary = path.with_suffix(".tmp.docx")
    with ZipFile(path) as source, ZipFile(temporary, "w", ZIP_DEFLATED) as target:
        for item in source.infolist():
            data = document_xml if item.filename == "word/document.xml" else source.read(item.filename)
            target.writestr(item, data)
    temporary.replace(path)


def build_contract(cfg: ContractConfig, render: bool) -> None:
    source = cfg.src.read_text(encoding="utf-8")
    source_sha256 = hashlib.sha256(cfg.src.read_bytes()).hexdigest()
    blocks = inject_language_notice(split_blocks(source), cfg)
    english_blocks: list[str] = []
    for block in blocks:
        if block.strip() == LANGUAGE_NOTICE.format(
            notary_de=cfg.notary_de, deed_de=cfg.deed_de, read_de=cfg.read_de
        ).strip():
            english_blocks.extend(split_blocks(LANGUAGE_NOTICE_EN.strip()))
            continue
        if block.strip() == PRIORITY_CLAUSE_DE.strip():
            english_blocks.extend(split_blocks(PRIORITY_CLAUSE_EN.strip()))
            continue
        english_blocks.append(translate_block(block))

    if len(blocks) != len(english_blocks):
        raise RuntimeError(f"Block count mismatch for {cfg.src}: {len(blocks)} != {len(english_blocks)}")

    out_dir = cfg.src.parent
    out_html = out_dir / f"{cfg.out_prefix}.html"
    out_pdf = out_dir / f"{cfg.out_prefix}.pdf"
    out_docx = out_dir / f"{cfg.out_prefix}.docx"
    html_text = html_document(
        f"{cfg.short_title} — Deutsch/English",
        bilingual_rows(blocks, english_blocks),
        source_sha256,
    )
    out_html.write_text(html_text, encoding="utf-8")

    if render:
        subprocess.run(["weasyprint", str(out_html), str(out_pdf)], check=True)
        tmp_odt = out_dir / f"{cfg.out_prefix}.odt"
        for stale in [tmp_odt, out_docx]:
            stale.unlink(missing_ok=True)
        subprocess.run(["soffice", "--headless", "--convert-to", "odt", "--outdir", str(out_dir), str(out_html)], check=True)
        subprocess.run(["soffice", "--headless", "--convert-to", "docx", "--outdir", str(out_dir), str(tmp_odt)], check=True)
        repair_bilingual_docx_tables(out_docx)
        tmp_odt.unlink(missing_ok=True)
        print(f"built {out_html.relative_to(ROOT)}, {out_pdf.relative_to(ROOT)}, {out_docx.relative_to(ROOT)}")
    else:
        print(f"built {out_html.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-render", action="store_true", help="Only generate bilingual HTML.")
    parser.add_argument(
        "--repair-docx",
        type=Path,
        help="Repair an already generated bilingual DOCX without running translation.",
    )
    args = parser.parse_args()

    if args.repair_docx is not None:
        repair_bilingual_docx_tables(args.repair_docx.resolve())
        print(f"repaired {args.repair_docx}")
        return

    for tool in ["pandoc"]:
        if shutil.which(tool) is None:
            raise SystemExit(f"Missing required tool: {tool}")
    if not args.no_render and shutil.which("weasyprint") is None:
        raise SystemExit("Missing required tool: weasyprint")
    if not args.no_render and shutil.which("soffice") is None:
        raise SystemExit("Missing required tool: soffice")

    for cfg in CONFIGS:
        build_contract(cfg, render=not args.no_render)


if __name__ == "__main__":
    main()
