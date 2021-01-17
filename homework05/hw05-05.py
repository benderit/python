#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#   Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
try:
	with open("testO.txt", "w") as fileO:
		a=input("Введите числа через пробел для записи в файл и Enter для завершения работы: ")
		fileO.write(f"{a}\n")

except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")

try:
	with open("testO.txt", "r") as fileO:
		line = fileO.readlines()[0][:-1]
except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")

print(line)
sum = 0

nums = line.split(" ")
for i in range(0, len(nums)):
	try:
		sum += float(nums[i].replace(",","."))
	except ValueError as err:
		print(err)

print(f"Sum of all elements in first line of the file: {sum}")