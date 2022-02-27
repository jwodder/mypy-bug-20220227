import attr
from .base import Widget

@attr.define
class BlueWidget(Widget):
    nessness: int = attr.field(init=False)

    def __attrs_post_init__(self) -> None:
        if self.app.nessess is None:
            raise ValueError("Blue widgets must be nessy")
        self.nessness = self.app.nessness
