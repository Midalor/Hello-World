type = input("Кто ваш питомец:")
name = input("Имя вашего питомца:")
age = int(input("Возраст вашего питомца:"))
if age >= 5 and age <= 20: 
    print("Это {} по имени {}. Возраст: {} лет.".format(type, name, age))
elif age % 10 == 1:
    print("Это {} по имени {}. Возраст: {} лет.".format(type, name, age))
elif 2 <= age % 10 <= 4:
    print("Это {} по имени {}. Возраст: {} лет.".format(type, name, age))
else:
    print("Это {} по имени {}. Возраст: {} лет.".format(type, name, age))
