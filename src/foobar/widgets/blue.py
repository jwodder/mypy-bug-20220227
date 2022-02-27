from dataclasses import dataclass, field
from .base import Widget


@dataclass
class BlueWidget(Widget):
    nessness: int = field(init=False)

    def __post_init__(self) -> None:
        if self.spec.nessness is None:
            raise ValueError("Blue widgets must be nessy")
        self.nessness = self.spec.nessness
