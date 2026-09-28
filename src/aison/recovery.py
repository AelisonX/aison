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


def format_recovery_steps(steps: list[RecoveryStep]) -> str:
    symbols = {
        StepStatus.COMPLETED: "✓",
        StepStatus.IN_PROGRESS: "→",
        StepStatus.PENDING: "○",
    }

    return "\n".join(
        f"{symbols[step.status]} {step.name}"
        for step in steps
    )