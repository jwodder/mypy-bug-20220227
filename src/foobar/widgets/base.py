from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ..app import App


@dataclass
class WidgetSpec:
    color: str
    flavor: str
    nessness: Optional[int]


@dataclass
class Widget:
    app: App
    spec: WidgetSpec
