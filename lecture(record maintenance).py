users = {}


def get_command():
    print()
    print("User record maintenance")
    print("V > view")
    print("A > add")
    print("U > update")
    print("D > delete")
    print("Q > quit")
    commands = input("Enter command:")
    return commands


def add():
    username = input("Key in username:")
    phone = input("Key in phone number:")
    email = input("Key in email:")
    user_info = {"phone": phone, "email": email}
    users[username] = user_info
    print(users[username])


def view():
    username = input("Key in username:")
    user_info = users.get(username)
    if not user_info:
        print("Record not found")
    else:
        print("Username: " + username)
        print("Phone: " + user_info["phone"])
        print("Email: " + user_info["email"])


def update():
    username = input("Key in username:")
    phone = input("Key in phone number:")
    email = input("Key in email:")
    user_info = users.get(username)
    if not user_info:
        print("Record not found")
    else:
        user_info["phone"] = phone
        user_info["email"] = email


def delete():
    username = input("Key in username:")
    user_info = users.get(username)
    if not user_info:
        print("Record not found")
    else:
        del users[username]


while True:
    command = get_command()

    if command == "V":
        view()
    elif command == "A":
        add()
    elif command == "U":
        update()
    elif command == "D":
        delete()
    elif command == "Q":
        quit()
        break
    else:
        print("Invalid Command")