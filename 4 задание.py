while True:
    num = input("Введите целое число: ")

    if num == "exit":
        print("Выход из программы...")
        break

    if num.lstrip('-').isdigit() and (num[0] != '-' or len(num) > 1):
        k = len(num.lstrip('-'))

        if k % 10 == 1 and k % 100 != 11:
            word = "цифра"
        elif 2 <= k % 10 <= 4 and not (11 <= k % 100 <= 15):
            word = "цифры"
        else:
            word = "цифр"

        print(f"В этом числе {k} {word}.")
    else:
        print("Ошибка: данные не являются целым числом.")