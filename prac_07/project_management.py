"""CP1404/CP5632 Practical - Project Management Program."""

import datetime
from project import Project

FILENAME = "projects.txt"


def main():
    """Run the Project Management Program."""
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "l":
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").lower()

    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save.startswith("y"):
        save_projects(FILENAME, projects)
    print("Thank you for using the Project Management software.")


def load_projects(filename):
    """Load projects from a tab-separated file."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-separated file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects separately."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]
    incomplete.sort()
    complete.sort()
    print("Incomplete projects:")
    for p in incomplete:
        print(" ", p)
    print("Completed projects:")
    for p in complete:
        print(" ", p)


def filter_projects_by_date(projects):
    """Show projects starting after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(" ", p)


def add_new_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))


def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
