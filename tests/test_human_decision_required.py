from aison.packet import Packet
from aison.synthesis import synthesize


def test_human_decision_required():
    packets = [
        Packet(
            packet_id="pkt_001",
            agent_id="ANALYST",
            status="ACCEPT",
        )
    ]

    decision = synthesize(
        packets=packets,
        decision_id="decision_test",
    )

    assert decision.human_decision_required is True