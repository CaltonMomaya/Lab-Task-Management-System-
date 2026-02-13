from datetime import datetime
from .validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index):
    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        return

    task = tasks[index - 1]
    if task["completed"]:
        print("Task is already completed.")
    else:
        task["completed"] = True
        print(f"Task '{task['title']}' marked as complete!")

def view_pending_tasks(tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks
    pending_tasks = [t for t in tasks_list if not t["completed"]]
    if not pending_tasks:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    for idx, t in enumerate(pending_tasks, start=1):
        print(f"{idx}. {t['title']} - Due: {t['due_date']}\n   Description: {t['description']}")
    print()

def calculate_progress(tasks_list=None):
    if tasks_list is None:
        tasks_list = tasks
    if not tasks_list:
        return 0.0
    completed_count = sum(1 for t in tasks_list if t["completed"])
    progress = (completed_count / len(tasks_list)) * 100
    return round(progress, 2)
