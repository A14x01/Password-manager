print("Welcome to password manager")

try:
    with open('password.txt', 'x') as f:
        f.close()
except:
    pass

def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[13:]+chars[:13]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )

def login():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data_login = (line.rstrip())
            while True:
                account_name_login = input("Account name: ")
                account_password_login = input("Account password: ")
                account_access = rot13((account_name_login + ":" + account_password_login))
                print(account_access)
                print(account_name_login)
                print(account_password_login)
                print(data_login)
                if account_access == data_login:
                    print("Welcome, " + account_name_login)
                    break
                else:
                    print("Wrong password or name, please try again.")
            break

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, password = data.split(":")
            print("User: ", rot13(user), "\nPassword: ", rot13(password))

def add():
    with open("password.txt", "r") as f:
        if f.readlines() == []:
            with open("password.txt", "a") as f:
                account_name = input("Account name: ")
                account_password = input("Account password: ")
                f.write(rot13(account_name + ":" + account_password + "\n"))
                print("Your first account has been created")
        else:
            with open("password.txt", "r") as f:
                for line in f.readlines():
                    saved_data = (line.rstrip())
                    user, password = saved_data.split(":")
                    while True:
                        with open("password.txt", "a") as f:
                            account_name = input("Account name: ")
                            account_password = input("Account password: ")
                            if account_name == rot13(user):
                                print("This account already exist")
                                pass
                            else:
                                f.write(rot13(account_name + ":" + account_password + "\n"))
                                print("New account has been created")
                                break
                    break

while True:
    print("If you want to sign in your account write login.")
    print("If you want to add new account write add.\nIf you want to view existing accounts write view.")
    mode = input("Press q to quit\n").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "login":
        login()
    else:
        print("Wrong mode")
        continue
#code made by https://github.com/A14x01
