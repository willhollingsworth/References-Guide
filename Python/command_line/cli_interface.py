import os

def clear_screen():
    os.system('cls')

def invalid_choice():
    print('invalid choice, please re-pick')
    wait_for_key()
    show_menu()

def wait_for_key():
    os.system('pause')

def show_menu():
    clear_screen()
    options = [1,2,3]
    menu = '''
    1. Option A
    2. Option B
    3. Exit
    '''
    print(menu)
    choice = input(" >>  ")
    try : choice = int(choice)
    except : invalid_choice()
    if choice in options:
        clear_screen()
        if choice == 1 : option_1()
        elif choice == 2 : option_2()
        elif choice == 3 : exit()
    else : invalid_choice()

def option_1():
    option_1 = '''
    welcome to option 1
    '''
    print(option_1)
    wait_for_key()
    show_menu()

def option_2():
    option_2 = '''
    welcome to option 1
    '''
    print(option_2)
    wait_for_key()
    show_menu()

if __name__ == '__main__':
    show_menu()