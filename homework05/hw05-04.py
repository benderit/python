#4. Создать (не программно) текстовый файл со следующим содержимым:
#   One — 1
#   Two — 2
#   Three — 3
#   Four — 4
#   Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
#   Новый блок строк должен записываться в новый текстовый файл.
def get_rus_numeric(digit):
	if(digit == 1):
		str = "Один"
	elif(digit == 2):
		str = "Два"
	elif(digit == 3):
		str = "Три"
	elif(digit == 4):
		str = "Четыре"

	return str

try:
	my_list = []
	with open("testO.txt", "r") as fileO:
		for line in fileO.readlines():
			line = line[:-1]
			words = line.split(" ")
			if(len(words) != 3):
				print(f"Line skipped, because have format error: Must be like \"One - 1\", but this is: {line}")
			else:
				try:
					digit = int(words[2].replace(",","."))
				except ValueError as err:
					print(f"Line skipped, because have format error: could not convert \"{words[2]}\" to int")
					my_list.append(f"{line}\n")
					continue
				rus_str = get_rus_numeric(digit)
				my_list.append(f"{rus_str} - {words[2]}\n")
except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")

print(my_list)
try:
	with open("testO_rus.txt", "w") as fileO:
		fileO.write(''.join(my_list))
except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")