from dataclasses import dataclass
from enum import Enum


class StepStatus(str, Enum):
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"


@dataclass(frozen=True)
class RecoveryStep:
    name: str
    status: StepStatus
    manual_instruction: str | None = None