from aison.recovery import RecoveryStep, StepStatus


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