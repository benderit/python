#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
try:
	with open("testO.txt", "r") as fileO:
		total_lines = 0
		for line in fileO.readlines():
			total_lines += 1
			words = len(line.split(" "))
			print(f"line: {total_lines}, line content: {line}words in line: {words}")
	print(f"\nTotal lines: {total_lines}")
except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")