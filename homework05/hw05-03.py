#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#   Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#   Выполнить подсчет средней величины дохода сотрудников.
try:
	with open("testO.txt", "r") as fileO:
		for line in fileO.readlines():
			line = line[:-1]
			words = line.split(" ")
			if(len(words) != 2):
				print(f"Line skipped, because have format error: Must be \"fio salary\", but this is: {line}")
			else:
				try:
					salary = float(words[1].replace(",","."))
				except ValueError as err:
					print(f"Line skipped, because have format error: could not convert \"{words[1]}\" to float")
					continue
				if(salary < 20_000):
					print(f"Low rate salary detected: {line}")
except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")