from aison.recovery import (
    RecoveryStep,
    StepStatus,
    format_recovery_steps,
    show_manual_instruction,
)


def test_recovery_step_can_store_status_and_manual_instruction():
    step = RecoveryStep(
        name="Commit change",
        status=StepStatus.IN_PROGRESS,
        manual_instruction="Select Commit changes and confirm the commit.",
    )

    assert step.name == "Commit change"
    assert step.status == StepStatus.IN_PROGRESS
    assert step.manual_instruction == "Select Commit changes and confirm the commit."


def test_recovery_step_manual_instruction_is_optional():
    step = RecoveryStep(
        name="Verify result",
        status=StepStatus.PENDING,
    )

    assert step.manual_instruction is None


def test_format_recovery_steps_shows_human_readable_progress():
    steps = [
        RecoveryStep(
            name="Open repository",
            status=StepStatus.COMPLETED,
        ),
        RecoveryStep(
            name="Commit change",
            status=StepStatus.IN_PROGRESS,
        ),
        RecoveryStep(
            name="Verify result",
            status=StepStatus.PENDING,
        ),
    ]

    result = format_recovery_steps(steps)

    assert result == (
        "✓ Open repository\n"
        "→ Commit change\n"
        "○ Verify result"
    )


def test_show_manual_instruction_returns_instruction():
    step = RecoveryStep(
        name="Commit change",
        status=StepStatus.IN_PROGRESS,
        manual_instruction="Select Commit changes and confirm the commit.",
    )

    assert show_manual_instruction(step) == (
        "Select Commit changes and confirm the commit."
    )


def test_show_manual_instruction_returns_none_when_missing():
    step = RecoveryStep(
        name="Verify result",
        status=StepStatus.PENDING,
    )

    assert show_manual_instruction(step) is None