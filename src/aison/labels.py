from enum import Enum


class EpistemicLabel(str, Enum):
    FACT = "FACT"
    INTERPRETATION = "INTERPRETATION"
    SPECULATION = "SPECULATION"
    MODEL_SELF_REPORT = "MODEL_SELF_REPORT"
    FICTION = "FICTION"
    JOKE = "JOKE"