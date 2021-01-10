#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
#   Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def add_user_data(user=None, name=None, surname=None, birthday=None, city=None, email=None, phone=None):
    if(not user):
        user = {'name': '', 'surname': '', 'birthday': '', 'city': '', 'email': '', 'phone': ''}
    
    if(name):
        user['name'] = name
    if(surname):
        user['surname'] = surname
    if(birthday):
        user['birthday'] = birthday
    if(city):
        user['city'] = city        
    if(email):
        user['email'] = email
    if(phone):
        user['phone'] = phone
        
    return user
    
print("Привет, эта программа просит ввести данные о пользователе, чтобы передать в функцию\n")



a=input("Введите имя для добавления или ввод для пропуска: ")
b=input("Введите фамилию для добавления или ввод для пропуска: ")
c=input("Введите дату рождения для добавления или ввод для пропуска: ")
d=input("Введите город проживания для добавления или ввод для пропуска: ")
e=input("Введите e-mail для добавления или ввод для пропуска: ")
f=input("Введите телефон для добавления или ввод для пропуска: ")

user = add_user_data(name=a, surname=b)
user = add_user_data(user=user, birthday=c)
user = add_user_data(user=user, city=d)
user = add_user_data(user=user, email=e)
user = add_user_data(user=user, phone=f)

print(user)