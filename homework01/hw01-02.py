#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
def str_time_format(int):
    if(int < 10):
        return '0'+str(int)
    else:
        return str(int)

print("Привет, эта программа конвертирует секунды в часовой формат HH:MM:SS\n")
a=int(input("Введите число секунд для преобразования: "))

days = 0
if(a > 86400):
    days = int(a / 86400)
    a = a - days*86400

H=int(a/3600)
M=int((a-H*3600)/60)
S=(a-H*3600-M*60)

if (days == 0):
    print(str_time_format(H)+":"+str_time_format(M)+":"+str_time_format(S))
else:
    print(str(days)+" days, "+str_time_format(H)+":"+str_time_format(M)+":"+str_time_format(S))

