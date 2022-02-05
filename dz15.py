from functions.login import login

if __name__ == '__main__':
    i = 1
    while i <= 3:
        login_username = str(input("Please enter your username.\n"))
        login_password = str(input("Please enter your password.\n"))
        if login(login_username, login_password):
            print("Вы в системе!")
            break
        else:
            if i == 3:
                print("Попытки истекли!")
            else:
                print("Не правильное Имя или Пароль У вас осталось {0} попыток".format(3 - i))
        i += 1

