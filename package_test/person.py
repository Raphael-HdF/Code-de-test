class Person:
    def __init__(self, first_name, last_name, age, pay=0, job=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.pay = pay
        self.job = job

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def give_raise(self, percent):
        self.pay *= 1.0 + percent

    def __str__(self):
        return f"{self.name} ({self.job})"


def main():
    persons = [
        Person('Andrea', 'Pillier', 42, job="soft engineer", pay=45000),
        Person('Olivier', 'Berger', 45, job="DevOps engineer", pay=43000),
    ]
    print(" & ".join(str(person) for person in persons))


main()
