import function
import view
import UI


def start():
    button = UI.menu()
    if button == 1:
        view.show(function.create_data())
        start()
    elif button == 2:
        function.get_data()
    elif button == 3:
        function.save_data()
    elif button == 4:
        print('До свидания!')
    else:
        print('Выберите цифру меню')
        start()
