from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)

        elif choice == "2":
            if not calculate_progress() and not tasks:  # Check if tasks list exists
                print("No tasks available to mark as complete.")
                continue
            print("\nAll Tasks:")
            for idx, t in enumerate(tasks, start=1):
                status = "Completed" if t["completed"] else "Pending"
                print(f"{idx}. {t['title']} - {status}")
            try:
                task_num = int(input("Enter task number to mark as complete: "))
                mark_task_as_complete(task_num)
            except ValueError:
                print("Invalid input. Enter a number.")

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            progress = calculate_progress()
            print(f"Overall Progress: {progress}%")

        elif choice == "5":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
