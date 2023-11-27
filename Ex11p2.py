import collections

# Словарь с информацией о питомцах
pets = {
    
}

# Функция создания новой записи
def create():
    last = collections.deque(pets, maxlen=1)[0]
    pet_id = last + 1
    name = input("Введите имя питомца: ")
    species = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    pets[pet_id] = {name: {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}}
    print("Запись успешно добавлена!")

# Функция чтения информации о питомце
def read():
    pet_id = int(input("Введите ID питомца: "))
    pet_info = get_pet(pet_id)
    if pet_info:
        pet_name = list(pet_info.keys())[0]
        pet_species = pet_info[pet_name]["Вид питомца"]
        pet_age = pet_info[pet_name]["Возраст питомца"]
        pet_owner = pet_info[pet_name]["Имя владельца"]
        print(f'Это {pet_species} по кличке "{pet_name}". Возраст питомца: {pet_age} {get_suffix(pet_age)}. Имя владельца: {pet_owner}')
    else:
        print("Питомец с указанным ID не найден!")

# Функция обновления информации о питомце
def update():
    pet_id = int(input("Введите ID питомца: "))
    pet_info = get_pet(pet_id)
    if pet_info:
        pet_name = list(pet_info.keys())[0]
        species = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner = input("Введите новое имя владельца: ")
        pets[pet_id][pet_name]["Вид питомца"] = species
        pets[pet_id][pet_name]["Возраст питомца"] = age
        pets[pet_id][pet_name]["Имя владельца"] = owner
        print("Информация о питомце успешно обновлена!")
    else:
        print("Питомец с указанным ID не найден!")

# Функция удаления питомца
def delete():
    pet_id = int(input("Введите ID питомца: "))
    pet_info = get_pet(pet_id)
    if pet_info:
        pet_name = list(pet_info.keys())[0]
        del pets[pet_id][pet_name]
        print("Питомец успешно удален!")
    else:
        print("Питомец с указанным ID не найден!")

# Функция получения информации о питомце по ID
def get_pet(ID):
    if ID in pets.keys():
        return pets[ID]
    else:
        return False

# Функция получения суффикса для возраста питомца
def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "года"
    else:
        return "лет"

# Функция отображения списка питомцев
def pets_list():
    for pet_id in pets.keys():
        pet_info = pets[pet_id]
        pet_name = list(pet_info.keys())[0]
        pet_species = pet_info[pet_name]["Вид питомца"]
        pet_age = pet_info[pet_name]["Возраст питомца"]
        pet_owner = pet_info[pet_name]["Имя владельца"]
        print(f'ID: {pet_id}, Питомец: {pet_name}, Вид: {pet_species}, Возраст: {pet_age}, Владелец: {pet_owner}')

# Главный цикл программы
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ")

    if command == "create":
        create()

    elif command == "read":
        read()

    elif command == "update":
        update()

    elif command == "delete":
        delete()

    elif command == "list":
        pets_list()

    elif command == "stop":
        print("Работа программы завершена")

    else:
        print("Неверная команда! Попробуйте еще раз.")
