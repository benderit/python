#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#   При вызове функции должен создаваться объект-генератор.
#   Функция должна вызываться следующим образом: for el in fact(n).
#   Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#   Подсказка: факториал числа n — произведение чисел от 1 до n.
#   Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
import memory_profiler
import sys
from datetime import datetime as dt
#2:16:54

def yelder(limit):
	cnt = 0
	while cnt <= limit:
		yield cnt
		cnt += 1

start = dt.now()
print(f"Start working at: {start}")
m1 = memory_profiler.memory_usage()
a = [x for x in range(100_000)]
mem_diff = memory_profiler.memory_usage()[0] - m1[0]

print(f"Finish at: {dt.now()}. Working time: {dt.now() - start}")
print(f"Size of objects: list: {round(sys.getsizeof(a)/1024/1024, 2)} Mb, Total: {round(mem_diff, 2)} Mb to execute this method")

start = dt.now()
print(f"\nStart working at: {start}")
m1 = memory_profiler.memory_usage()
a = yelder(100_000)
l = [el for el in a]
mem_diff = memory_profiler.memory_usage()[0] - m1[0]

print(f"Finish at: {dt.now()}. Working time: {dt.now() - start}")
print(f"Size of objects: list: {round(sys.getsizeof(l)/1024/1024, 2)} Mb, Total: {round(mem_diff, 2)} Mb to execute this method")