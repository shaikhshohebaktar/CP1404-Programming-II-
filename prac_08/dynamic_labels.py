"""
CP1404/CP5632 Practical 08
Dynamic Labels Demo
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """DynamicLabelsApp creates labels dynamically from a list of names."""

    def build(self):
        """Build the app using the kv layout and add labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")

        # Example data (list of names)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

        # Create and add a Label for each name
        for name in self.names:
            temp_label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(temp_label)

        return self.root


if __name__ == "__main__":
    DynamicLabelsApp().run()
