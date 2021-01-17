#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#   Пример строки файла: firm_1 ООО 10000 5000.
#   Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#   Если фирма получила убытки, в расчет средней прибыли ее не включать.
#   Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#   Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#   Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#   Итоговый список сохранить в виде json-объекта в соответствующий файл.
#   Пример json-объекта:
#   [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
#   Подсказка: использовать менеджеры контекста.
import json

profit_sum = 0
profit_companys = 0
companys = {}

try:
	with open('companys.json', encoding='utf-8') as fileO:
		for line in fileO.readlines():
			data = json.loads(line[:-1])
			for list in data:
				cname = list
				ownership = data[list]["ownership"]
				profit = int(data[list]["revenue"]) - int(data[list]["expenses"])
				if (profit > 0):
					profit_companys += 1
					profit_sum += profit
				companys[cname] = profit

except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")

average_profit = profit_sum / profit_companys
result_list = [companys, {"average_profit": average_profit}]
print(result_list)

try:
	with open("companys_profit.json", "w") as write_file:
	    json.dump(result_list, write_file)

except IOError as err:
    print(f"Ошибка ввода-вывода: {err}")