class BaseClass:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def greet(self):
        return f"Hello, my name is {self.name}."

    def describe(self):
        return f"I am {self.gender}."


class DerivedClass(BaseClass):
    def __init__(self, name, age, gender):
        super().__init__(name, gender)
        self.age = age

    def greet(self):
        base_greet = super().greet()
        return f"{base_greet} I am {self.age} years old."

    def is_adult(self):
        return self.age >= 18

    def describe(self):
        base_describe = super().describe()
        return f"{base_describe[:-1]} and I am {self.age} years old."
