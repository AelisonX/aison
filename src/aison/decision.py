from dataclasses import dataclass, field
from typing import List


@dataclass
class Decision:
    decision_id: str
    status: str

    consensus: List[str] = field(default_factory=list)
    dissent: List[str] = field(default_factory=list)
    unknown: List[str] = field(default_factory=list)
    provenance_gaps: List[str] = field(default_factory=list)

    human_decision_required: bool = True