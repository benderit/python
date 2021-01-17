#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
#   практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
#   Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#   Примеры строк файла:
#   Информатика: 100(л) 50(пр) 20(лаб).
#   Физика: 30(л) — 10(лаб)
#   Физкультура: — 30(пр) —
#
#   Пример словаря:
#   {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import json

try:
	with open('lections.json', encoding='utf-8') as fileO:
		data = json.load(fileO)

except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")

for list in data:
	print(f"{list}: {data[list]}")
	if(data[list].get("lections")):
		print(data[list]["lections"])
	if(data[list].get("practics")):
		print(data[list]["practics"])
	if(data[list].get("labs")):
		print(data[list]["labs"])