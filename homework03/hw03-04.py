#4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. 
#   Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#   Подсказка: попробуйте решить задачу двумя способами. 
#   Первый — возведение в степень с помощью оператора **.
#   Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func(x, y):
    res = x*1
    for i in range(abs(y)-1):
        res = res * x
    
    if(y < 0):
        res = 1/res
        
    return res
    
print("Привет, эта программа возводит x в степень y")
print("Введите 2 числа через пробел, затем Enter\n")

while True:
    a=input("Введите 2 числа или Enter для завершения: ")
    if(len(a) == 0):
        break
    
    list=a.split(" ")
    if(len(list) == 2):
        f_x = float(list[0])
        int_y = int(list[1])
        res = my_func(f_x, int_y)
        print(res)
        continue