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
    decrypted_users = []
    decrypted_passwords = []
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data_login = (line.rstrip())
            user, password = data_login.split(":")
            decrypted_user = rot13(user)
            decrypted_password = rot13(password)
            decrypted_users.append(decrypted_user)
            decrypted_passwords.append(decrypted_password)
        while True:
            try:
                account_name = input("Account name:")
                index_of_user = decrypted_users.index(account_name)
            except:
                print("Wrong")
                continue
            account_password = input("Account password:")
            if decrypted_passwords[index_of_user] == account_password:
                print("Welcome, " + account_name)
                break
            elif decrypted_user != account_name:
                print("Wrong username.")
            elif decrypted_password != account_password:
                print("Wrong password.")
            else:
                print("Wrong password or name, please try again.")

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


while True:
    print("\nIf you want to sign in your account write login.")
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
