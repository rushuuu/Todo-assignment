import pytest
from src.todo_manager import ToDoListManager, Task


@pytest.fixture
def manager():
    return ToDoListManager()


def test_add_task(manager):
    task = manager.add_task("Test Task", "2025-01-07")
    assert task.description == "Test Task"
    assert task.due_date == "2025-01-07"
    assert not task.completed


def test_mark_task_complete(manager):
    task = manager.add_task("Test Task", "2025-01-07")
    manager.mark_task_complete(task.id)
    assert manager.tasks[task.id].completed


def test_list_tasks(manager):
    manager.add_task("Task 1", "2025-01-07")
    manager.add_task("Task 2", "2025-01-08")
    assert len(manager.list_tasks()) == 2
    assert len(manager.list_tasks(completed=False)) == 2


def test_delete_task(manager):
    task = manager.add_task("Test Task", "2025-01-07")
    manager.delete_task(task.id)
    assert len(manager.tasks) == 0
