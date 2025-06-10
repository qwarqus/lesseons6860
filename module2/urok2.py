from logging.config import stopListening

phonenumber = {}
print("1. Додати контакт")
print("2. Пошук контакту")
print("3. Видалити контакт")


answer = input("Введіть команду: ")
if answer == "1":
    key = input("Input name")
    value = input("Input number")
    phonenumber[key] = value
    print(f'контакт: {key} додано')
    print(phonenumber)


if answer == "2":
    # get()
    key = input("Введіть ім'я для пошуку: ")
    print(f'{key}: {phonenumber.get(key, "контакт знайдено")}')

if answer == "3":
    key = input("Введіть ім'я для видалення: ")
    answer = phonenumber.pop(key)
    if removed:
        print(f'Контакт {key} видалено.')
    else:
        print("Контакт не знайдено.")
