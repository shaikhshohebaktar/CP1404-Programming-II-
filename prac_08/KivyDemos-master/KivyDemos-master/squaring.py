"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """SquareNumberApp is a Kivy App for squaring a number."""
    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle the calculation when the 'Square' button is pressed."""
        try:
            number = float(value)
            result = number ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            # If input is invalid, do not crash — just show nothing
            self.root.ids.output_label.text = ""


SquareNumberApp().run()
