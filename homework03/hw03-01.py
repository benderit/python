#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#   Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(a, b):
    if(b == 0):
        return "На 0 делить нельзя"
    else:
        return a/b

print("Привет, эта программа делит 2 числа через функцию, с проверкой на 0\n")

a=input("Введите число1: ")
b=input("Введите число2: ")

f_a = float(a.replace(",", "."))
f_b = float(b.replace(",", "."))
res = division(f_a, f_b)
print(f"a/b = {res}")