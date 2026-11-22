"""Run the two text turns in an empty directory. Keep expected results outside the input."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]
CASE = Path(__file__).with_name("dialog.json")
MODEL = "gpt-6.2-astra"
SETTING = (
    "Wende den beigefügten eigenständigen Werkstatt-Prompt auf den aktuellen Auftrag an. "
    "Du arbeitest in einem reinen Textchat und erhältst die vollständigen für diese Runde "
    "bereitgestellten Unterlagen als Markdown. Nutze keine Werkzeuge. Gib die bestellten "
    "drei Dokumente in der Antwort vollständig aus. Kein tatsächlicher Versand."
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def content(relative):
    path = (ROOT / relative).resolve()
    path.relative_to(ROOT)
    return path.read_bytes()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Neuer Ordner für Antworten und Laufmetadaten")
    parser.add_argument("--skill-revision", help="Optionaler Git-Stand des zu ladenden Skilltexts")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    case = json.loads(CASE.read_bytes())
    if args.skill_revision:
        revision = subprocess.check_output(
            ["git", "rev-parse", "--verify", "--end-of-options", args.skill_revision + "^{commit}"],
            cwd=ROOT, text=True,
        ).strip()
        skill = subprocess.check_output(["git", "show", revision + ":" + case["skill"]], cwd=ROOT)
    else:
        skill = content(case["skill"])
    metadata = {
        "fall": case["fall"], "modell": MODEL,
        "cli": subprocess.check_output(["codex", "--version"], text=True).strip(),
        "basis_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "skill": case["skill"], "skill_sha256": sha(skill), "runden": [],
    }
    history = []
    with tempfile.TemporaryDirectory(prefix="mw02-blind-") as empty:
        for turn in case["runden"]:
            number = turn["runde"]
            sources = [(path, content(path)) for path in turn["eingaben"]]
            question = "\n\n".join(f"## {Path(p).name}\n\n{b.decode('utf-8')}" for p, b in sources)
            prompt = "\n\n".join([SETTING, "<Arbeitsprompt>\n" + skill.decode() + "\n</Arbeitsprompt>",
                                  *history, "<Nutzeranfrage>\n" + question + "\n</Nutzeranfrage>"])
            command = [
                "codex", "exec", "--ignore-user-config", "--skip-git-repo-check", "--ephemeral", "--json",
                "--disable", "multi_agent", "--disable", "shell_tool", "--disable", "unified_exec",
                "--sandbox", "read-only", "--model", MODEL, "-c", 'model_reasoning_effort="high"',
                "-c", 'web_search="disabled"', "-C", empty, "-",
            ]
            result = subprocess.run(command, input=prompt, cwd=empty, text=True, capture_output=True,
                                    timeout=300, check=True)
            events = [json.loads(line) for line in result.stdout.splitlines() if line.strip()]
            items = [e["item"] for e in events if "item" in e]
            nontext = {item["type"] for item in items} - {"reasoning", "agent_message"}
            if nontext or not any(e.get("type") == "turn.completed" for e in events):
                raise RuntimeError(f"Runde {number} nicht als abgeschlossener Text-Blindlauf nutzbar: {nontext}")
            texts = [e["item"]["text"] for e in events if e.get("type") == "item.completed"
                     and e["item"]["type"] == "agent_message"]
            if not texts or not texts[-1].strip():
                raise RuntimeError(f"Leere Antwort in Runde {number}")
            answer = texts[-1]
            artifact = output / f"mw02-antwort-{number}.md"
            artifact.write_text(answer + "\n", encoding="utf-8")
            history += ["<Frühere_Nutzeranfrage>\n" + question + "\n</Frühere_Nutzeranfrage>",
                        "<Frühere_Antwort>\n" + answer + "\n</Frühere_Antwort>"]
            metadata["runden"].append({
                "runde": number, "eingaben": {p: sha(b) for p, b in sources},
                "zugestellter_text_sha256": sha(prompt.encode()), "antwort": artifact.name,
                "antwort_sha256": sha(artifact.read_bytes()), "werkzeugaufrufe": [],
                "tokens": next(e["usage"] for e in events if e.get("type") == "turn.completed"),
            })
            print(f"Runde {number}: {len(answer)} Zeichen, keine Werkzeuge", flush=True)
    (output / "mw02-lauf.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
                                          encoding="utf-8")


if __name__ == "__main__":
    main()
