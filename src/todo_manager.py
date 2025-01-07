import uuid
from datetime import datetime

# Create a class Task with constructor id description duedate completed

class Task:
    def __init__(self, description: str, due_date: str):
        self.id = str(uuid.uuid4())
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __repr__(self):
        return f"Task(id={self.id}, description={self.description}, due_date={self.due_date}, completed={self.completed})"

class ToDoListManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description: str, due_date: str):
        if not description or not due_date:
            raise ValueError("Description and due date are required.")
        try:
            datetime.fromisoformat(due_date)
        except ValueError:
            raise ValueError("Due date must be in ISO format (YYYY-MM-DD).")
        
        task = Task(description, due_date)
        self.tasks[task.id] = task
        return task

    def mark_task_complete(self, task_id: str):
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        self.tasks[task_id].completed = True

    def list_tasks(self, completed=None):
        if completed is None:
            return list(self.tasks.values())
        return [task for task in self.tasks.values() if task.completed == completed]

    def delete_task(self, task_id: str):
        if task_id not in self.tasks:
            raise ValueError("Task not found.")
        del self.tasks[task_id]    