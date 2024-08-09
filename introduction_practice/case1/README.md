# Задача: 
Дан одномерный массив А размерности N. Найти сумму отрицательных элементов, расположенных между максимальным и минимальным. 

## Описание функций

1. **`find_minmax_indexes`**: Эта функция принимает массив чисел и возвращает индексы минимального и максимального элементов массива. Если массив пуст, функция выбрасывает исключение `ValueError`.

2. **`find_negative_sum`**: Эта функция принимает массив чисел и возвращает сумму всех отрицательных чисел между минимальным и максимальным элементами массива (включительно или исключительно в зависимости от параметра `inclusive`). Если массив пуст, функция возвращает 0.

## Пример использования

```python
from solution import find_minmax_indexes, find_negative_sum

arr = [1, -4, 3, -2, 5]

min_index, max_index = find_minmax_indexes(arr)
print(f"Min index: {min_index}, Max index: {max_index}") # "Min index: 1, Max index: 4"

negative_sum = find_negative_sum(arr, inclusive=True)
print(f"Negative sum (inclusive): {negative_sum}") # -6

negative_sum_exclusive = find_negative_sum(arr, inclusive=False)
print(f"Negative sum (exclusive): {negative_sum_exclusive}") # -2
