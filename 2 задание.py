number = input("Введите число: ")

if number.replace('.', '', 1).lstrip('-').isdigit():
    num = float(number)
    if num == 0:
        print("Введён ноль (0)")
    elif num < 0 or num % 1 != 0:
        print("Число не является целым положительным")
    else:
        if num % 2 == 0:
            print("Число является чётным")
        else:
            print("Число не является чётным")
else:
    print("Введено не число")