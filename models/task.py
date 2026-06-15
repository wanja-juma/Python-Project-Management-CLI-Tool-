class Task:
    """Task within a project."""

    def __init__(self, title):
        self.title = title
        self.status = "pending"
        self.contributors = []

    def mark_complete(self):
        self.status = "completed"

    def add_contributor(self, user_id):
        if user_id not in self.contributors:
            self.contributors.append(user_id)