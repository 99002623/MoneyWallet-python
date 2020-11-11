from menu2 import clear_screen, menu2


def login(acc_list):

    login_id = input('Please, Enter your info(press "Ctrl+C" to go back) \n>>ID: ')
    login_password = input('>>Password: ')
    found = False
    for account in acc_list:
        if account[0] == login_id and account[2] == login_password:
            found = True
            clear_screen()
            menu2(account)
            break
        else:
            continue


