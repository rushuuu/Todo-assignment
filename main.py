from src.todo_manager import ToDoListManager

def main():
    manager = ToDoListManager()

    print("ToDo List Manager")
    task1 = manager.add_task("Induction started", "2025-01-06")
    task2 = manager.add_task("Advertisement World", "2025-01-07")
    task3 = manager.add_task("Product Demo", "2025-01-07")
    print(f"Task added: {task1}")
    print(f"Task added: {task2}")
    print(f"Task added: {task3}")

    print("\nListing all tasks:")
    for task in manager.list_tasks():
        print(task)

    print("\nMarking first task as complete...")
    manager.mark_task_complete(task1.id)

    print("\nListing completed tasks:")
    for task in manager.list_tasks(completed=True):
        print(task)

    print("\nListing pending tasks:")
    for task in manager.list_tasks(completed=False):
        print(task)    

    print("\nDeleting third task...")
    manager.delete_task(task3.id)

    print("\nListing all tasks after deletion:")
    for task in manager.list_tasks():
        print(task)


if __name__ == "__main__":
    main()
