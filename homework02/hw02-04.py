#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
#   Вывести каждое слово с новой строки. 
#   Строки необходимо пронумеровать. 
#   Если в слово длинное, выводить только первые 10 букв в слове.
print("Привет, эта программа разбивает строку по словам\n")
txt=input("Введите текст: ")
list = txt.split(" ")
i = 0
for word in list:
    i = i + 1
    print(f"{i}. {word[0:10]}")