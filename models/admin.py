from models.user import User

class Admin(User):
    """Admin user with elevated role."""

    def display_info(self):
        return f"Admin: {self.name}"