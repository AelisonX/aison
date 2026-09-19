from typing import List

from .decision import Decision
from .packet import Packet


def synthesize(packets: List[Packet], decision_id: str) -> Decision:
    decision = Decision(
        decision_id=decision_id,
        status="PROVISIONAL",
    )

    for packet in packets:
        if packet.status == "ACCEPT":
            decision.consensus.append(packet.agent_id)

        elif packet.status == "DISSENT":
            decision.dissent.append(packet.agent_id)

        elif packet.status == "UNKNOWN":
            decision.unknown.append(packet.agent_id)

        if packet.integrity_warning:
            decision.provenance_gaps.append(packet.agent_id)

    if decision.dissent or decision.unknown or decision.provenance_gaps:
        decision.status = "UNRESOLVED"

    decision.human_decision_required = True

    return decision