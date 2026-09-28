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
    safe_checkpoint: bool = False


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


def show_manual_instruction(step: RecoveryStep) -> str | None:
    return step.manual_instruction


def can_take_over(step: RecoveryStep) -> bool:
    return step.safe_checkpoint