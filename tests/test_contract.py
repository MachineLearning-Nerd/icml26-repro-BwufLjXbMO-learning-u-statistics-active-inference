import json
from pathlib import Path


def test_live_contract_has_six_claims():
    claims = json.loads(Path('contract/live_claims.json').read_text())
    assert len(claims) == 6
    assert all(item['status'] == 'unverified' for item in claims)


def test_source_manifest_exists():
    manifest = Path('evidence/SHA256SUMS')
    assert manifest.exists()
    assert 'arxiv_source.tar' in manifest.read_text()
