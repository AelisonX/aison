expected_agents = ["ANALYST", "RED_TEAM", "SYNTHESIZER"]

received = {
    "ANALYST": "ACCEPT",
    "SYNTHESIZER": "ACCEPT",
}

print("COUNCIL STATUS")
print("--------------")

for agent in expected_agents:
    status = received.get(agent, "UNKNOWN")
    print(f"{agent}: {status}")

missing = [
    agent
    for agent in expected_agents
    if agent not in received
]

print()

if missing:
    print("PACKET_INTEGRITY_WARNING")
    print(f"Missing expected input: {', '.join(missing)}")
    print()
    print("Consensus: NOT ESTABLISHED")
    print("Human decision required: YES")
else:
    print("Packet integrity: PASS")