from view import show
from view import add_contact

def show_the_directory():
    show()
    print()
    start_phone_book()

def add_in_directory():
    add_contact()
    print()
    start_phone_book()

def exit(): 
    print('Конец работы')

def start_phone_book():
    print('Программа *Телефонный справочник* \n     текстовая альфа-версия\n')
    menu = int(input("Выберите действие:" 
    "\n1 - показать все контакты"
    "\n2 - добавить контакт"
    "\n3 - выйти из программы\n"))
    if menu == 1:
        show_the_directory()
    elif menu == 2:
        add_in_directory()
    elif menu == 3: exit()