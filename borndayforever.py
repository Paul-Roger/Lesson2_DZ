while True:
    user_input = "nop"
    while not user_input.isdigit():
        user_input = input("Введите год рождения А.С.Пушкина: ")
    if int(user_input) == 1799:
        break
    else:
        print("неверный год рождения")

while True:
    user_input = "nop"
    while not user_input.isdigit():
        user_input = input("Введите день рождения А.С.Пушкина: ")
    if  int(user_input) == 26:
        print("верно")
        break
    else:
        print("неверный день рождения")
