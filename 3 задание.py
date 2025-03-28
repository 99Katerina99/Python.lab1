age = input("Введите ваш возраст: ")

if age.lstrip('-').isdigit():
    if int(age) < 0:
        print("Ошибка: возраст не может быть отрицательным!")
    elif 18 > int(age) > 0 :
        print("Вы несовершеннолетний.")
    elif int(age) == 0:
        print("Недопустимый возраст!")
    elif int(age) >= 120:
        print("Недопустимый возраст!")
    else:
        print("Вы совершеннолетний.")
else:
    print("Ошибка: введено не число.")


