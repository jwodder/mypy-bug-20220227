from .widgets import Widget, RedWidget, BlueWidget, WidgetSpec
import attr

class App:
    def make_widget(spec: WidgetSpec) -> Widget:
        if spec.color == "red":
            return RedWidget(app=self, spec=spec)
        elif spec.color == "blue":
            return BlueWidget(app=self, spec=spec)
        else:
            raise ValueError(f"Unsupported widget color: {spec.color!r}")
