from enum import Enum


class EvidenceStatus(str, Enum):
    LIT = "LIT"
    ENG = "ENG"
    HYP = "HYP"
    UNK = "UNK"
