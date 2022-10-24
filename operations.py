def open_base(file_name):
    file = open(file_name, "r", encoding="utf-8-sig")
    uni_base = file.readlines()
    return uni_base


def add_new_row(current_base, new_row_lst):
    new_id_string = current_base[-1].split(';')
    new_id = str(int(new_id_string[0]) + 1)
    result = f'{new_id};{new_row_lst[0]};{new_row_lst[1]};{new_row_lst[2]};{new_row_lst[3]};{new_row_lst[4]}'
    current_base.append(result)
    return current_base


def delete_row(current_base, number_of_row):
    current_base_list = []
    for i in current_base:
        i = i.split(';')
        current_base_list.append(i)
    current_base_list.pop(number_of_row)
    for j in range(number_of_row, len(current_base_list)):
        current_base_list[j][0] = str(j)
    for k in range(len(current_base_list)):
        current_base_list[k] = ";".join(map(str, current_base_list[k]))
        current_base = current_base_list
    return current_base


def save_base(current_base, file_name):
    file = open(file_name, "w", encoding="utf-8-sig")
    for i in current_base:
        file.writelines(i)


def show_base(current_base):
    for line in current_base:
        print(line)


def show_row(current_base, row_number):
    print(current_base[0])
    print(current_base[row_number])
