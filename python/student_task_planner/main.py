
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load saved tasks, or return an empty list."""
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved tasks.")
    return []


def save_tasks(tasks):
    """Save tasks to a JSON file."""
    DATA_FILE.write_text(
        json.dumps(tasks, indent=4),
        encoding="utf-8",
    )


def add_task(tasks):
    title = input("Enter assignment or task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one to get started!")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))
        if not 1 <= number <= len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tasks[number - 1]["completed"] = True
    save_tasks(tasks)
    print("Task marked as complete!")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== Student Task Planner ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Good luck with your studies!")
            break
        else:
            print("Invalid choice. Please choose 1–4.")


if __name__ == "__main__":
    main()
