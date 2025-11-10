from project import Project
from datetime import datetime


def main():
    projects = load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")

    menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Filename: ")
            save_project(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_data(projects)
        elif choice == "A":
            projects.append(add_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option")
        menu()
        choice = input(">>> ").upper()

    save_choice = input("Save project.txt? (Y/N)").upper()
    if save_choice == "Y":
        save_project("projects.txt", projects)


def menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    projects = []
    with open(filename, "r") as filename:
        filename.readline()
        for line in filename:
            name, start_time, priority, cost, percent = line.strip().split("\t")
            project = Project(name, start_time, int(priority), float(cost), int(percent))
            projects.append(project)
    return projects


def display_projects(projects):
    incomplete = [p for p in projects if p.completion_percentage < 100]
    complete = [p for p in projects if p.completion_percentage == 100]

    print("Incomplete projects: ")
    for p in sorted(incomplete):
        print(" ", p)

    print("Complete projects: ")
    for p in sorted(complete):
        print(" ", p)


def add_project():
    name = input("Name: ")
    start_time = input("Start time (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost Estimate: "))
    percent = int(input("Completion percentage: "))
    return Project(name, start_time, priority, cost, percent)


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    index = int(input("Project choice: "))
    project = projects[index]

    new_percentage = input("New completion percentage:")
    if new_percentage:
        project.completion_percentage = int(new_percentage)

    new_priority = input("new priority:")
    if new_priority:
        project.priority = int(new_priority)


def filter_projects_by_data(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered = [p for p in projects if p.start_date >= filter_date]
    for p in sorted(filtered):
        print(" ", p)


def save_project(filename, projects):
    with open(filename, "r") as filename:
        filename.write("Name Start date Cost Estimate Completion Percentage")
    for p in projects:
        filename.write(f"{p.name}{p.start_date:%d/%m/%Y}{p.priority}{p.cost_estimate}{p.completion_percentage}")


main()
