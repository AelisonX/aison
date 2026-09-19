def test_missing_is_not_consent():
    expected_agents = ["ANALYST", "RED_TEAM", "SYNTHESIZER"]

    received = {
        "ANALYST": "ACCEPT",
        "SYNTHESIZER": "ACCEPT",
    }

    missing = [
        agent
        for agent in expected_agents
        if agent not in received
    ]

    consensus_reached = len(missing) == 0

    assert "RED_TEAM" in missing
    assert consensus_reached is False