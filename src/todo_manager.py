from typing import List, Optional

class Task:
    id_counter = 1  

    def __init__(self, description: str, due_date: str):
        self.id = Task.id_counter
        Task.id_counter += 1  
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __repr__(self):
        return f"Task(id={self.id}, description={self.description}, due_date={self.due_date}, completed={self.completed})"


class ToDoListManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description: str, due_date: str) -> Task:
        if not description.strip():
            raise ValueError("Task description cannot be empty.")
        if not due_date.strip():
            raise ValueError("Due date cannot be empty.")
        task = Task(description, due_date)
        self.tasks[task.id] = task
        return task

    def mark_task_complete(self, task_id: int):
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist.")
        self.tasks[task_id].completed = True

    def list_tasks(self, filter_by: Optional[str] = None) -> List[Task]:
        if filter_by is None:
            return list(self.tasks.values())
        elif filter_by == "completed":
            return [task for task in self.tasks.values() if task.completed]
        elif filter_by == "pending":
            return [task for task in self.tasks.values() if not task.completed]
        else:
            raise ValueError("Invalid filter. Use 'completed', 'pending', or None.")

    def delete_task(self, task_id: int):
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} does not exist.")
        del self.tasks[task_id]
