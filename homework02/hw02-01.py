#1. Создать список и заполнить его элементами различных типов данных. 
#   Реализовать скрипт проверки типа данных каждого элемента. 
#   Использовать функцию type() для проверки типа. 
#   Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
import types

def print_by_type(my_list, checktype):
    filtered = []
    if(type(checktype) is not list):
        checktype = [checktype]

    for element in my_list:
        for typ in checktype:
            if(type(element) is typ):
                filtered.append(element)
    print(filtered)

print("Привет, эта программа проверяет тип данных в элементах списка\n")
my_list = [None, 'string', 10, 10.1, complex(1, 2), b'\xd0', bytearray(b'hello world!'), u'x', ['this','is','list'], (1, 2, 3), {'dict': 1, 'dictionary': 2}]

print("Список объектов и их тип в нашем листе:")
for element in my_list:
    print(f"{type(element)} {element}")

print("\nОтфильтроанный список по категории строки: ")
print_by_type(my_list, str)

print("\nОтфильтроанный список по категории числа: ")
print_by_type(my_list, [int, float])

print("\nОтфильтроанный список по категории массивы данных: ")
print_by_type(my_list, [str, bytearray, list, tuple, dict])