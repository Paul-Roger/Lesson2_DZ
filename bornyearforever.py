while True:
    user_input = "nop"
    while not user_input.isdigit():
        user_input = input("Введите год рождения А.С.Пушкина: ")

    if int(user_input) == 1799:
        print("верно")
        break
    else:
        print("неверно")