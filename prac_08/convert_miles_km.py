"""
CP1404 Practical
Convert Miles to Kilometres Kivy App
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    """App to convert miles to kilometres."""
    output_km = StringProperty("0.0")

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Miles to Kilometres Converter"
        return Builder.load_file("convert_miles_km.kv")

    def handle_convert(self):
        """Convert miles to kilometres."""
        miles = self._get_valid_miles()
        km = miles * MILES_TO_KM
        self.output_km = f"{km:.3f}"

    def handle_increment(self, change):
        """Increase or decrease the miles value."""
        miles = self._get_valid_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def _get_valid_miles(self):
        """Return the miles value as float, or 0.0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


if __name__ == "__main__":
    ConvertMilesKmApp().run()
