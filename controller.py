import operations
import UI

process = True

UI.start_message()
base = operations.open_base(UI.open_base_message())

while process == True:
    choise = UI.choise_message()
    if choise == 1:
        operations.show_base(base)
    elif choise == 2:
        operations.show_row(base, UI.show_row_message())
    elif choise == 3:
        base = operations.add_new_row(base, UI.show_new_row())
    elif choise == 4:
        base = operations.delete_row(base, UI.show_delete_row())
    elif choise == 5:
        operations.save_base(base, UI.show_save_base())
    else:
        exit()
