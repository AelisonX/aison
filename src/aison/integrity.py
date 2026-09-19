from typing import List

from .packet import Packet


def check_packet_integrity(packet: Packet) -> bool:
    expected = set(packet.expected_previous_steps)
    received = set(packet.received_previous_steps)

    missing = expected - received

    packet.integrity_warning = bool(missing)

    return not packet.integrity_warning