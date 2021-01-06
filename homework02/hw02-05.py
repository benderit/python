#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
#   У пользователя необходимо запрашивать новый элемент рейтинга. 
#   Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#	Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#	Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#	Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#	Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#	Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
print("Привет, эта программа формирует невозрастающий список\n")
my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    a=input("Введите элемент для добавления или ввод для завершения: ")
    if(len(a) == 0):
        break
    
    a = int(a)
    
    i = len(my_list)
    while i > 0:
        i = i - 1
        if( my_list[i] >= a):
            i = i + 1
            break

    my_list.insert(i, a)

    print(my_list)