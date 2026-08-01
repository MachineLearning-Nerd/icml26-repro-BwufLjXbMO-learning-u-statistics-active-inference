#!/usr/bin/env python3
"""One literal-source falsification attempt for live Claim 6.

This tests the stated comparators and quantities against the pinned accepted
TeX. It deliberately treats unavailable experiment artifacts as a replication
limitation, never as a counterexample.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "upstream" / "arxiv_source" / "ICML_Camera-ready.tex"
OUT = ROOT / "outputs" / "claim6_falsification_result.json"


def line(text: str, needle: str) -> int:
    for number, value in enumerate(text.splitlines(), 1):
        if needle in value:
            return number
    raise ValueError(f"missing source phrase: {needle}")


def main() -> None:
    text = TEX.read_text()
    live = json.loads((ROOT / "contract" / "live_claims.json").read_text())[5]["text"]
    source_sentence = (
        "It requires approximately 20\\% less budget than {classical} baseline "
        "to achieve the same inferential accuracy, and about 10\\% less budget "
        "than {uniform} sampling."
    )
    checks = {
        "live_names_political_bias": "political-bias dataset" in live,
        "live_names_kendall_tau": "Kendall" in live,
        "live_names_twenty_vs_classical": "20% versus the classical baseline" in live,
        "live_names_ten_vs_uniform": "10% versus uniform sampling" in live,
        "source_names_political_bias": "Political bias dataset" in text,
        "source_names_kendall_tau": "Kendall's $\\tau$ coefficient" in text,
        "source_sentence_present": source_sentence in text,
        "source_does_not_swap_comparators": (
            "20\\% less budget than {uniform} sampling" not in text
            and "10\\% less budget than {classical} baseline" not in text
        ),
    }
    if not all(checks.values()):
        raise SystemExit(f"literal-comparator checks failed: {checks}")

    result = {
        "claim": 6,
        "attempt": "falsification",
        "outcome": "inconclusive",
        "scope": "literal live-claim versus pinned-source comparator/quantity audit; no numerical proxy",
        "live_claim": live,
        "source_tex_sha256": hashlib.sha256(TEX.read_bytes()).hexdigest(),
        "source_lines": {
            "political_task": line(text, "Political bias dataset"),
            "kendall_target": line(text, "Kendall's $\\tau$ coefficient"),
            "literal_comparator_sentence": line(text, source_sentence),
        },
        "checks": checks,
        "reason": (
            "No literal source contradiction was found: the pinned source states "
            "the same political-bias/Kendall target and assigns about 20% budget "
            "saving to classical and about 10% to uniform. Missing numerical "
            "artifacts prevent independent replication but are not treated as a falsification."
        ),
        "next_action": "logbook_assembly_and_independent_review",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
