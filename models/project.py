class Project:
    """Represents a project."""

    def __init__(self, title, description, due_date, user_id):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_id = user_id
        self.tasks = []

    def add_task(self, task_id):
        if task_id not in self.tasks:
            self.tasks.append(task_id)