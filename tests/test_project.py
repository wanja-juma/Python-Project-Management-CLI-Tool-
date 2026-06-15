from models.project import Project

def test_add_task():
    project = Project(
        "CLI Tool",
        "Build tracker",
        "2026-12-31",
        "user-1"
    )

    project.add_task("task-1")

    assert "task-1" in project.tasks