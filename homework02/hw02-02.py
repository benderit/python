#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
#   При нечетном количестве элементов последний сохранить на своем месте. 
#   Для заполнения списка элементов необходимо использовать функцию input().
list = []
print("Привет, эта программа переставляет элементы местами\n")

while True:
    a=input("Введите элемент для добавления или ввод для завершения: ")
    if(len(a) == 0):
        break
    else:
        list.append(a)

l = len(list)
for i in range(l - l % 2 -1):
    if(i % 2 == 0):
        list[i], list[i+1] = list[i+1], list[i]

print("Перетасованный список: ")
for i in range(len(list)):
    print(f"{list[i]}")