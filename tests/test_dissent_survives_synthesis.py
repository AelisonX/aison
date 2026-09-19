from aison.packet import Packet
from aison.synthesis import synthesize


def test_dissent_survives_synthesis():
    packets = [
        Packet(
            packet_id="pkt_001",
            agent_id="ANALYST",
            status="ACCEPT",
        ),
        Packet(
            packet_id="pkt_002",
            agent_id="RED_TEAM",
            status="DISSENT",
        ),
    ]

    decision = synthesize(
        packets=packets,
        decision_id="decision_test",
    )

    assert "RED_TEAM" in decision.dissent
    assert decision.status == "UNRESOLVED"