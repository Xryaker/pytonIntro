from functions.login import login
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', type=str, help="input username")
parser.add_argument('-p', '--password', type=str, help="input password")
space = parser.parse_args()
if __name__ == '__main__':
    i = 1
    while i <= 3:
        if space.username is not None:
            login_username = str(space.username)
        else:
            login_username = str(input("Please enter your username.\n"))
        if space.password is not None:
            login_password = str(space.password)
        else:
            login_password = str(input("Please enter your password.\n"))

        if login(login_username, login_password):
            print("Вы в системе!")
            break
        else:
            if i == 3:
                print("Попытки истекли!")
            else:
                print("Не правильное Имя или Пароль У вас осталось {0} попыток".format(3 - i))
                space.username = None
                space.password = None
        i += 1
