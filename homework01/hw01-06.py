#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
#   Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. 
#   Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. 
#   Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
print("Привет, эта программа вычислит сколько дней нужно для достижения результата в беге\n")
a1=float(input("Сколько километров пробежал спортсмен в 1й день?: ").replace(",", "."))
b1=float(input("Сколько километров должен спортсмен пробегать за день?: ").replace(",", "."))

d = 1
x = a1
while x < b1:
    x = float(x*1.1)
    d = d + 1

print("Цель будет достигнута на "+str(d)+" день")