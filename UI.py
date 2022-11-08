def start_message():
    print('Перед началом работы необходимо открыть базу данных')
    print('---' * 17)


def open_base_message():
    name = input('Введите имя файла базы данных в формате "name.csv": ')
    return name


def choise_message():
    print('---' * 20)
    print('Выберите действие:\n'
          '1: Вывод на экран текущей базы данных\n'
          '2: Вывод на экран определенной строки из текущей базы данных\n'
          '3: Добавить новую запись в текущую базу данных\n'
          '4: Удалить запись из текущей базы данных\n'
          '5: Сохранить базу данных\n'
          '6: Завершение работы')
    print('---' * 20)
    choise = int(input('Выберите вариант: '))
    while choise > 6 or choise < 1:
        choise = int(input('Выберите вариант от 1 до 6: '))
    return choise


def show_row_message():
    row = int(input('Введите id записи для показа: '))
    return row


def show_new_row():
    new_row_list = []
    add_name = input('Введите параметр "Имя" новой записи: ')
    new_row_list.append(add_name)
    add_surname = input('Введите параметр "Фамилия" новой записи: ')
    new_row_list.append(add_surname)
    add_birth_date = input('Введите параметр "Дата рождения" новой записи: ')
    new_row_list.append(add_birth_date)
    add_phone_number = input(
        'Введите параметр "Номер телефона" новой записи: ')
    new_row_list.append(add_phone_number)
    add_facultet = input('Введите параметр "Факультет" новой записи: ')
    new_row_list.append(add_facultet)
    return new_row_list


def show_delete_row():
    delete_row_id = int(input('Для удаления записи введите id строки: '))
    return delete_row_id


def show_save_base():
    save_file_name = input(
        'Введите имя файла для сохранения базы данных в формате "name.csv": ')
    return save_file_name
