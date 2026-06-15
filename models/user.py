from models.person import Person

class User(Person):
    """System user (developer)."""

    user_count = 0

    def __init__(self, name, email):
        super().__init__(name, email)
        User.user_count += 1

        self.id = User.user_count
        self.projects = []

    def add_project(self, project_id):
        if project_id not in self.projects:
            self.projects.append(project_id)

    def display_info(self):
        return f"User: {self.name}"