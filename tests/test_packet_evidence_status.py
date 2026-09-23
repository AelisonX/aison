from aison.evidence import EvidenceStatus
from aison.packet import Packet


def test_packet_can_carry_evidence_status():
    packet = Packet(
        packet_id="pkt_001",
        agent_id="ANALYST",
        status="ACCEPT",
        evidence_status=EvidenceStatus.HYP,
    )

    assert packet.evidence_status is EvidenceStatus.HYP


def test_packet_evidence_status_is_optional():
    packet = Packet(
        packet_id="pkt_002",
        agent_id="ANALYST",
        status="UNKNOWN",
    )

    assert packet.evidence_status is None
