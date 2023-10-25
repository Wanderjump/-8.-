from logger import input_data, print_data, edit_data, del_data

def interface():
    print("Доброго времени суток! Это бот Микола! \n"
          "Что вы хотите сделать?\n"
          "1 - Записать данные \n"
          "2 - Вывести данные \n"
          "3 - Редактировать данные \n"
          "4 - Удалить данные")
    command = int(input("Ваш выбор: "))

    while command < 1 or command > 4:
        command = int(input("Ошибка! Ваш выбор: "))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        del_data()
