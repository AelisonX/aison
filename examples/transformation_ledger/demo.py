from dataclasses import dataclass, field
from typing import List


@dataclass
class TransformationRecord:
    step: str
    preserved: List[str] = field(default_factory=list)
    altered: List[str] = field(default_factory=list)
    lost: List[str] = field(default_factory=list)
    introduced: List[str] = field(default_factory=list)


def print_record(record: TransformationRecord) -> None:
    print(f"\n=== {record.step} ===")

    sections = [
        ("Preserved", record.preserved),
        ("Altered", record.altered),
        ("Lost", record.lost),
        ("Introduced", record.introduced),
    ]

    for title, items in sections:
        print(f"\n{title}:")
        if items:
            for item in items:
                print(f"- {item}")
        else:
            print("- None")


def main() -> None:
    original_statement = (
        "Compare two approaches without choosing for me. "
        "Keep uncertainty visible and preserve minority objections."
    )

    print("ORIGINAL INPUT")
    print(original_statement)

    pipeline = [
        TransformationRecord(
            step="Step 1 — Summarizer",
            preserved=[
                "comparison between two approaches",
                "request not to choose",
                "uncertainty should remain visible",
            ],
            altered=[
                "wording compressed",
            ],
            lost=[
                "explicit instruction to preserve minority objections",
            ],
            introduced=[],
        ),
        TransformationRecord(
            step="Step 2 — Critic",
            preserved=[
                "comparison framing",
                "visible uncertainty",
            ],
            altered=[
                "focus shifted toward trade-offs and implementation risks",
            ],
            lost=[],
            introduced=[
                "implementation-cost framing",
            ],
        ),
        TransformationRecord(
            step="Step 3 — Synthesizer",
            preserved=[
                "comparison",
                "uncertainty",
                "implementation-cost framing",
            ],
            altered=[
                "multiple viewpoints merged into a shorter final structure",
            ],
            lost=[
                "one minority objection",
            ],
            introduced=[
                "a concise decision summary",
            ],
        ),
    ]

    for record in pipeline:
        print_record(record)


if __name__ == "__main__":
    main()