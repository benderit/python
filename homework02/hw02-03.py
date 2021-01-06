#3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
#   Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
#   Напишите решения через list и через dict.
seasons = ("Зима", "Весна", "Лето", "Осень")
s_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
s_dict = {0: s_list[0], 1: s_list[1], 2: s_list[2], 3: s_list[3]}

print("Привет, эта программа скажет какое время года относится к введенному месяцу\n")
month=int(input("Введите номер месяца: "))

for i in range(len(s_list)):
    if(month in s_list[i]):
        print(seasons[i])
        break
    
for season in s_dict:
    if(month in s_dict[season]):
        print(seasons[season])
        break