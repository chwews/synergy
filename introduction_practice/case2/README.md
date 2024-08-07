# Задача: 
Написать тестовую программу, которая демонстрирует работу методов базового и производного классов

## Описание классов

1. **`BaseClass`**: Базовый класс, который принимает имя и пол в качестве параметров и имеет методы `greet` и `describe`.

2. **`DerivedClass`**: Производный класс, который наследует от `BaseClass`, добавляет возраст и методы `is_adult`, а также переопределяет методы `greet` и `describe`.

## Пример использования

```python
from classes import BaseClass, DerivedClass

person = BaseClass("Alice", "female")
print(person.greet())       # "Hello, my name is Alice."
print(person.describe())    # "I am female."

student = DerivedClass("Bob", 20, "male")
print(student.greet())      # "Hello, my name is Bob. I am 20 years old."
print(student.describe())   # "I am male and I am 20 years old."
print(student.is_adult())   # True
