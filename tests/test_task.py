from models.task import Task


def test_task_creation():
    """Test that a task is created with default values."""

    task = Task("Build CLI")

    assert task.title == "Build CLI"
    assert task.status == "pending"
    assert task.contributors == []


def test_mark_task_complete():
    """Test that a task can be marked as completed."""

    task = Task("Write tests")

    task.mark_complete()

    assert task.status == "completed"


def test_add_contributor():
    """Test adding contributors to a task."""

    task = Task("Implement feature")

    task.add_contributor("user-1")
    task.add_contributor("user-2")

    assert "user-1" in task.contributors
    assert "user-2" in task.contributors
    assert len(task.contributors) == 2


def test_no_duplicate_contributors():
    """Ensure duplicate contributors are not added."""

    task = Task("Fix bug")

    task.add_contributor("user-1")
    task.add_contributor("user-1")

    assert len(task.contributors) == 1