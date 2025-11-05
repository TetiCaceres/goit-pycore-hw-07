from datetime import datetime

class Field:
    """Base class for record fields."""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Represents the name of a contact."""
    pass

class Phone(Field):
    """Represents a validated 10-digit phone number."""
    def __init__(self, value):
        self.value = self.is_valid(value)

    def is_valid(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        return value

class Birthday(Field):
    """Represents a valid birthday in DD.MM.YYYY format."""
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")