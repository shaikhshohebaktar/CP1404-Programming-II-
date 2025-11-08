"""CP1404 Practical  Guitar class"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year

    def is_vintage(self) -> bool:
        """Determine if the guitar is 50 or more years old."""
        return 2025 - self.year >= 50
