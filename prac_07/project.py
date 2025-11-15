"""CP1404 Practical  Project class"""

import datetime

class Project:
    """Represent a project with name, start date, priority, cost estimate and completion percentage."""

    def __init__(self, name: str, start_date: datetime.date, priority: int,
                 cost_estimate: float, completion_percentage: int):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority (for sorting)."""
        return self.priority < other.priority

    def is_complete(self) -> bool:
        """Return True if the project is 100% complete."""
        return self.completion_percentage == 100
