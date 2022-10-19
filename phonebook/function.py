def create_data():
    import random
    from datetime import date
    global id
    global name
    global birthdate
    global phone1
    global phone2
    id = []
    name = []
    birthdate = []
    phone1 = []
    phone2 = []
    n = int(input('Введите размер справочника в строках '))
    for i in range(n*1):
        id.append(i)
        name.append('Name-' + str(i))
        birthdate.append(date.today().replace(day=random.randint(
            1, 30), month=random.randint(1, 12), year=random.randint(1940, 2010)))
        phone1.append(random.randint(79010000001, 79999999999))
        phone2.append(random.randint(74950000001, 74999999999))
    return id, name, birthdate, phone1, phone2


def save_data():
    global id
    global name
    global birthdate
    global phone1
    global phone2

    with open('gb_python_homework/phonebook/phonebook.csv', 'w') as file:
        file.write('ID Name  Birthdate  MobilePhone  HomePhone'+"\n")
        for i in id:
            file.writelines(str(id[i])+" "+name[i]+" "+str(birthdate[i]) +
                            " "+str(phone1[i])+" "+str(phone2[i])+"\n")


def get_data():
    with open('gb_python_homework/phonebook/phonebook.csv', "r") as file1:
        for line in file1:
            # print('ID Name  Birthdate  MobilePhone  HomePhone')
            print(line.strip())
