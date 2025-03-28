name = str(input("Ваше имя:"))
surname = str(input("Фамилия:"))
age = int(input("Возраст:"))

print("\nРеализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {}".format(name, surname,age))

print("\nРеализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age}")

