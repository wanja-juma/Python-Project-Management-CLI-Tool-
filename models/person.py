class Person:
    """Base class for all people."""

    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value