#victory - famous writers and their birthyears

famous_name = ["А.С.Пушкин","М.Ю.Лермонтов","И.С.Тургенев","Л.Н.Толстой","И.А.Бунин"]
famous_year = [1799, 1814, 1818, 1828, 1870]

while True:
    i = 0
    points = 0
    exit_code = 0
    print("укажите год рождения следующеих авторов:")
    for i in range(5):
        user_input = input(famous_name[i] + "> ")
        while not user_input.isdigit():
            user_input = input(famous_name[i] + "> ")

        if int(user_input) == famous_year[i]:
            points +=1
    print("правильных ответов:   " + str(points) + " - " + str(points*100/5) + " %")
    print("неправильных ответов: " + str(5-points) + " - " + str((5-points) * 100 / 5) + " %")

    while True:
        user_input = input("Хотите начать заново (да/нет)? ")
        if  user_input == "нет" or user_input == "Нет" or user_input == "НЕТ":
            exit_code = 0
            break
        elif  user_input == "да" or user_input == "Да" or user_input == "ДА":
            exit_code = 1
            break
        else:
            exit_code = 9
    if exit_code == 0:
        break
