from models.user import User

def test_add_project():
    user = User("Alex", "alex@test.com")

    user.add_project("proj-1")

    assert "proj-1" in user.projects