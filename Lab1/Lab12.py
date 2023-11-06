print("Общество в начале XXI века")

while True:
    age = int(input("Введите ваш возраст: "))

    if 0 <= age <= 7:
        print("Вам в детский сад")
    elif 7 < age <= 18:
        print("Вам в школу")
    elif 18 < age <= 25:
        print("Вам в профессиональное учебное заведение")
    elif 25 < age <= 60:
        print("Вам на работу")
    elif 60 < age <= 120:
        print("Вам предоставляется выбор")
    else:
        print("Ошибка! Это программа для людей!\n" * 5)

    
    another_age = input("Хотите ввести еще один возраст? (да/нет): ")
    if another_age.lower() != 'да':
        break
