
"""Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

from random import randint


# Первый вариант с O(n^2)
def serch_min_value1(lst):
    for i in lst:  # O(N)
        is_min = True
        for j in lst:  # O(N)
            if i > j:
                is_min = False
        if is_min:
            return i
            # итого  0(N)*O(N)= O(N2)

# Второй вариант с O(n)
def serch_min_value2(lst):
    min_value = lst[0]
    for i in lst:  # O(N)
        if i < min_value:
            min_value = i
    return min_value
# итого O(N) = O(N)

lst1 = [randint(0, 10) for i in range(1)]
print(lst1)
print(serch_min_value1(lst1))
print(serch_min_value2(lst1))
