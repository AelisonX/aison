from aison.recovery import (
    RecoveryStep,
    StepStatus,
    can_start_again,
    can_take_over,
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


def test_can_take_over_returns_true_for_safe_checkpoint():
    step = RecoveryStep(
        name="Review change",
        status=StepStatus.IN_PROGRESS,
        safe_checkpoint=True,
    )

    assert can_take_over(step) is True


def test_can_take_over_returns_false_for_unsafe_checkpoint():
    step = RecoveryStep(
        name="External action in progress",
        status=StepStatus.IN_PROGRESS,
        safe_checkpoint=False,
    )

    assert can_take_over(step) is False


def test_can_start_again_returns_true_for_replayable_checkpoint():
    step = RecoveryStep(
        name="Review change",
        status=StepStatus.COMPLETED,
        replayable_checkpoint=True,
    )

    assert can_start_again(step) is True


def test_can_start_again_returns_false_for_non_replayable_checkpoint():
    step = RecoveryStep(
        name="Payment submitted",
        status=StepStatus.COMPLETED,
        replayable_checkpoint=False,
    )

    assert can_start_again(step) is False


def test_takeover_and_replayability_are_independent():
    step = RecoveryStep(
        name="Review change",
        status=StepStatus.COMPLETED,
        safe_checkpoint=False,
        replayable_checkpoint=True,
    )

    assert can_take_over(step) is False
    assert can_start_again(step) is True