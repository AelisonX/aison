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
    replayable_checkpoint: bool = False


@dataclass(frozen=True)
class RecoverySession:
    capability: str
    steps: tuple[RecoveryStep, ...]


def format_recovery_steps(
    steps: list[RecoveryStep] | tuple[RecoveryStep, ...]
) -> str:
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


def can_start_again(step: RecoveryStep) -> bool:
    return step.replayable_checkpoint


def current_step(session: RecoverySession) -> RecoveryStep | None:
    for step in session.steps:
        if step.status == StepStatus.IN_PROGRESS:
            return step

    return None


def latest_takeover_checkpoint(
    session: RecoverySession,
) -> RecoveryStep | None:
    for step in reversed(session.steps):
        if (
            step.safe_checkpoint
            and step.status != StepStatus.PENDING
        ):
            return step

    return None


def latest_restart_checkpoint(
    session: RecoverySession,
) -> RecoveryStep | None:
    for step in reversed(session.steps):
        if (
            step.replayable_checkpoint
            and step.status != StepStatus.PENDING
        ):
            return step

    return None