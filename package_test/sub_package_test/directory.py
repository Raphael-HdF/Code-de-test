from operator import attrgetter

class Person:

    def __init__(self, first_name, name, email):
        self.first_name = first_name
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        self._name = str(value).lower()

    @property
    def first_name(self):
        return self._first_name.title()

    @first_name.setter
    def first_name(self, value):
        self._first_name = str(value).lower()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in str(value) and "." not in str(value):
            raise ValueError("goto hell")
        self._email = str(value).lower()

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("other must be person")
        return (
                self.name == other.name
                and self.first_name == other._first_name
                and self.email == other.email
        )

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("other must be person")
        return (self.name, self.first_name, self.email) < (
            other.name,
            other._first_name,
            other.email
        )

    def __str__(self):
        return f"{self.name} {self.first_name} {self.email}"


class Directory:
    """Represents a directory of people."""

    def __init__(self):
        """Initializes a new directory."""
        self._persons = []

    def __str__(self):
        """Returns a string representation of the directory."""
        return str([str(person) for person in self._persons])

    # Implement this method. Eventually modify the signature of the method.
    def add(self, *persons):
        """Adds new persons to the directory."""
        for person in persons:
            if not isinstance(person, Person):
                raise ValueError("Must be a Person")
            self._persons.append(person)
            # self._persons.sort(key=attrgetter('name'), )
            self._persons = sorted(self._persons, key=lambda x: (x.name, x.first_name))

directory = Directory()
directory.add(
    Person(first_name="Guido", name="van Rossom", email="bdfl@python.org"),
    Person(
        first_name="Adrian", name="Holovaty", email="bdfl@djangoproject.com"
    )
)
for person in directory._persons:
    print(person.email)
print(directory)
