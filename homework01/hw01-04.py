#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
print("Привет, эта программа ищет максимальну цифру в числе\n")
s=input("Введите число: ")

i = len(s)-1
x = int(s)
max = x % 10
while i > 0:
    x = x // 10 
    a = x % 10
    if( a > max):
        max = a
    i = i - 1
    
print("Наивысший знак в числе: " + str(max))