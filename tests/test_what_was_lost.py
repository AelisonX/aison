from aison.packet import Packet
from aison.synthesis import synthesize


def test_unresolved_decision_names_what_was_lost():
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
        decision_id="decision_loss",
    )

    assert decision.status == "UNRESOLVED"
    assert "DISSENT:RED_TEAM" in decision.what_was_lost


def test_clean_accept_loses_nothing():
    packets = [
        Packet(
            packet_id="pkt_003",
            agent_id="ANALYST",
            status="ACCEPT",
        ),
    ]

    decision = synthesize(
        packets=packets,
        decision_id="decision_clean",
    )

    assert decision.what_was_lost == []