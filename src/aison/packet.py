from dataclasses import dataclass, field
from typing import List, Optional

from .evidence import EvidenceStatus


@dataclass
class Packet:
    packet_id: str
    agent_id: str
    status: str

    evidence_status: Optional[EvidenceStatus] = None
    parent_packet_id: Optional[str] = None

    source_ids: List[str] = field(default_factory=list)
    expected_previous_steps: List[str] = field(default_factory=list)
    received_previous_steps: List[str] = field(default_factory=list)

    integrity_warning: bool = False
