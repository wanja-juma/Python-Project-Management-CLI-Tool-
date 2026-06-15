from models.user import User
from models.project import Project
from models.task import Task


def test_user_to_projects():
    user = User("Alex", "alex@test.com")
    user.add_project("P1")
    user.add_project("P2")

    assert len(user.projects) == 2


def test_project_to_tasks():
    project = Project("CLI", "desc", "2026-12-31", "1")

    project.add_task("T1")
    project.add_task("T2")

    assert "T1" in project.tasks


def test_task_to_contributors():
    task = Task("Build CLI")

    task.add_contributor("U1")
    task.add_contributor("U2")

    assert "U1" in task.contributors
    assert "U2" in task.contributors