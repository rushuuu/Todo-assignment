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