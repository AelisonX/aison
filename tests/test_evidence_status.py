from aison.evidence import EvidenceStatus


def test_evidence_status_values():
    assert EvidenceStatus.LIT.value == "LIT"
    assert EvidenceStatus.ENG.value == "ENG"
    assert EvidenceStatus.HYP.value == "HYP"
    assert EvidenceStatus.UNK.value == "UNK"
