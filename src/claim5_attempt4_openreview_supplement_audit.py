#!/usr/bin/env python3
"""Attempt-4 primary-source supplement-access audit for Claim 5.

This is a new official-source route after the VitalDB, author/GitHub, and arXiv
source-package checks. It records OpenReview forum/API access outcomes; it does
not infer absence of a supplement from an access control response.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence" / "claim5_attempt4"
OUT_DIR = ROOT / "outputs" / "claim5_attempt4"
OUT = OUT_DIR / "result.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    forum = EVIDENCE / "openreview_forum.html"
    forum_status = (EVIDENCE / "openreview_forum.status").read_text().strip()
    endpoints = (EVIDENCE / "endpoints.tsv").read_text().strip().splitlines()
    api_statuses = sorted(path.read_text().strip() for path in EVIDENCE.glob("api_*.status"))
    if forum_status != "200" or "Please complete the verification above" not in forum.read_text(errors="replace"):
        raise SystemExit("expected retained public OpenReview verification response")
    if api_statuses != ["403", "403"]:
        raise SystemExit(f"expected two retained OpenReview API 403 responses, got {api_statuses}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "claim": 5,
        "attempt": 4,
        "outcome": "inconclusive",
        "scope": "official OpenReview supplement-access audit only; no proxy VitalDB experiment or claim verdict inference from access control",
        "forum_http_status": forum_status,
        "forum_turnstile_present": True,
        "api_http_statuses": api_statuses,
        "queried_endpoints": endpoints,
        "evidence_sha256": {
            path.name: sha256(path)
            for path in sorted(EVIDENCE.iterdir())
            if path.is_file() and path.name != "SHA256SUMS"
        },
        "source_faithful_rerun_possible": False,
        "finding": "The public forum returns a verification challenge and both public note API routes return 403. This does not prove no supplement exists; it leaves any non-public attachment unavailable to the autonomous CPU reproduction.",
        "next_action": "continue Claim 5 only if a new public, source-faithful VitalDB protocol/data artifact becomes available; otherwise retain inconclusive evidence and proceed with other claim/logbook milestones",
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
