import pytest
from solution import BaseClass, DerivedClass

def test_base_class_greet():
    person = BaseClass("Alice", "female")
    assert person.greet() == "Hello, my name is Alice."

def test_base_class_describe():
    person = BaseClass("Alice", "female")
    assert person.describe() == "I am female."

def test_derived_class_greet():
    student = DerivedClass("Bob", 20, "male")
    assert student.greet() == "Hello, my name is Bob. I am 20 years old."

def test_derived_class_is_adult_true():
    adult = DerivedClass("Charlie", 25, "male")
    assert adult.is_adult() == True

def test_derived_class_is_adult_false():
    child = DerivedClass("Daisy", 15, "female")
    assert child.is_adult() == False

def test_derived_class_describe():
    student = DerivedClass("Eva", 30, "female")
    assert student.describe() == "I am female and I am 30 years old."

if __name__ == "__main__":
    pytest.main()
