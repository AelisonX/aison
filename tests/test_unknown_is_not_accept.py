def test_unknown_is_not_accept():
    status = "UNKNOWN"

    assert status != "ACCEPT"