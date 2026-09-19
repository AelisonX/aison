from aison.integrity import check_packet_integrity
from aison.packet import Packet
from aison.synthesis import synthesize


analyst = Packet(
    packet_id="pkt_001",
    agent_id="ANALYST",
    status="ACCEPT",
)

red_team = Packet(
    packet_id="pkt_002",
    agent_id="RED_TEAM",
    status="DISSENT",
    expected_previous_steps=["ANALYST"],
    received_previous_steps=["ANALYST"],
)

synthesizer = Packet(
    packet_id="pkt_003",
    agent_id="SYNTHESIZER",
    status="UNKNOWN",
    expected_previous_steps=["ANALYST", "RED_TEAM"],
    received_previous_steps=["ANALYST"],
)

packets = [analyst, red_team, synthesizer]

for packet in packets:
    check_packet_integrity(packet)

decision = synthesize(
    packets=packets,
    decision_id="decision_001",
)

print("AISØN COUNCIL DEMO")
print("------------------")
print(f"Status: {decision.status}")
print(f"Consensus: {decision.consensus}")
print(f"Dissent: {decision.dissent}")
print(f"Unknown: {decision.unknown}")
print(f"Provenance gaps: {decision.provenance_gaps}")
print(f"Human decision required: {decision.human_decision_required}")