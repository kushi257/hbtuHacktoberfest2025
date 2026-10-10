# Student Task Planner

A beginner-friendly command-line application that helps students keep track of assignments and study tasks.

## Features

- Add new assignments or tasks.
- View all tasks and their completion status.
- Mark tasks as completed.
- Save tasks automatically so they remain available after restarting the program.
- Handle invalid menu choices and task numbers.

## Requirements

- Python 3.8 or later
- No external libraries required.

## How to Run

1. Download or clone the repository.
2. Open a terminal in the `python/student_task_planner` folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

## How to Use

1. Select `1` to add an assignment.
2. Select `2` to view all assignments.
3. Select `3` to mark an assignment as completed.
4. Select `4` to exit.

Tasks are stored in `tasks.json`, which is created automatically when you add a task.

## Concepts Demonstrated

- Functions and loops
- Lists and dictionaries
- User input and validation
- JSON file handling
- Python's standard library
