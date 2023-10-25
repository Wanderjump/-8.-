from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формат записать даные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')



def print_data():
    print("1 Вариант: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 Вариант: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="")


def edit_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формат записать даные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "w", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "w", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def del_data():
    with open("data_first_variant.csv", "w", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            i = ''

    print("2 Вариант: ")
    with open("data_second_variant.csv", "w", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            i = ''