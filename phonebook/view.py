def show(data):
    id, name, birthdate, phone1, phone2 = data
    result = ''
    print('ID Name  Birthdate  MobilePhone  HomePhone')
    
    for i in id:
        result = str(id[i]) + " " + str(name[i]) + " " + str(birthdate[i]) + " " + str(phone1[i]) + " " + str(phone2[i])
        print(result)