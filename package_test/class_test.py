from .sub_package_test.sub_class_test import first_kwarg


class Person:

    def __init__(self, name="Serge"):
        self.name = name

    @staticmethod
    def say_hello():
        print("Hello")


# def Person():
#     print("fuck")
def main():
    first_kwarg("Hello")


main()
