from src.todo_manager import ToDoListManager

def main():
    manager = ToDoListManager()

    print("Adding tasks...")
    task1 = manager.add_task("Buy groceries", "2025-01-10")
    task2 = manager.add_task("Complete project report", "2025-01-15")
    print(f"Task added: {task1}")
    print(f"Task added: {task2}")

    print("\nListing all tasks:")
    for task in manager.list_tasks():
        print(task)

    print("\nMarking first task as complete...")
    manager.mark_task_complete(task1.id)

    print("\nListing completed tasks:")
    for task in manager.list_tasks(completed=True):
        print(task)

    print("\nDeleting second task...")
    manager.delete_task(task2.id)

    print("\nListing all tasks after deletion:")
    for task in manager.list_tasks():
        print(task)


if __name__ == "__main__":
    main()
