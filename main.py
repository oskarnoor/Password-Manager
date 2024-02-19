import random
import string


chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)


def generate_password(n):
    return "".join(random.choice(chars) for _ in range(n))


def encrypter(web, name, pwd):
    new_name = ""
    new_pwd = ""

    true_name = ""
    true_pwd = ""
    key = random.randint(1, 1)
    if key == 1:
        key = [
            ">",
            "*",
            "K",
            "Y",
            "W",
            "?",
            "1",
            "%",
            "$",
            " ",
            "8",
            "s",
            "k",
            "=",
            "`",
            "M",
            ";",
            "\\",
            "2",
            "/",
            "4",
            "b",
            "B",
            "~",
            "&",
            "c",
            "3",
            ":",
            "<",
            "h",
            "L",
            "v",
            "j",
            "l",
            ".",
            "|",
            '"',
            "n",
            "P",
            "F",
            "_",
            "C",
            "G",
            "^",
            "Q",
            "(",
            "z",
            "6",
            "o",
            "r",
            "q",
            "D",
            "g",
            "X",
            "y",
            "]",
            "i",
            "}",
            "u",
            "p",
            "t",
            "{",
            "[",
            "!",
            "0",
            "x",
            "A",
            "J",
            "T",
            "+",
            "w",
            "a",
            "'",
            "#",
            "@",
            "Z",
            "m",
            "N",
            "V",
            "7",
            "R",
            ")",
            "O",
            "d",
            "9",
            "S",
            "E",
            "f",
            "-",
            ",",
            "H",
            "e",
            "U",
            "I",
            "5",
        ]
        for letter in name:
            index = chars.index(letter)
            new_name += key[index]
        for letter in pwd:
            index = chars.index(letter)
            new_pwd += key[index]
        true_name += (
            "X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz"
            + new_name
            + "81^1mnfa.,1&adFra1*13T1maul/1dADmb"
        )
        true_pwd += (
            "X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz"
            + new_pwd
            + "81^1mnfa.,1&adFra1*13T1maul/1dADmb"
        )

    return web, true_name, true_pwd


def decrypt(line):
    line = line.split("0000000")
    web = line[0]
    name = line[1]
    pwd = line[2]

    name_new = []
    pwd_new = []
    if (
        "81^1mnfa.,1&adFra1*13T1maul/1dADmb" in name
        and "X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz" in name
    ):
        key = [
            ">",
            "*",
            "K",
            "Y",
            "W",
            "?",
            "1",
            "%",
            "$",
            " ",
            "8",
            "s",
            "k",
            "=",
            "`",
            "M",
            ";",
            "\\",
            "2",
            "/",
            "4",
            "b",
            "B",
            "~",
            "&",
            "c",
            "3",
            ":",
            "<",
            "h",
            "L",
            "v",
            "j",
            "l",
            ".",
            "|",
            '"',
            "n",
            "P",
            "F",
            "_",
            "C",
            "G",
            "^",
            "Q",
            "(",
            "z",
            "6",
            "o",
            "r",
            "q",
            "D",
            "g",
            "X",
            "y",
            "]",
            "i",
            "}",
            "u",
            "p",
            "t",
            "{",
            "[",
            "!",
            "0",
            "x",
            "A",
            "J",
            "T",
            "+",
            "w",
            "a",
            "'",
            "#",
            "@",
            "Z",
            "m",
            "N",
            "V",
            "7",
            "R",
            ")",
            "O",
            "d",
            "9",
            "S",
            "E",
            "f",
            "-",
            ",",
            "H",
            "e",
            "U",
            "I",
            "5",
        ]
        name = name.replace("X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz", "")
        name = name.replace("81^1mnfa.,1&adFra1*13T1maul/1dADmb", "")
        for letter in name:
            index = key.index(letter)
            name_new += chars[index]

    if (
        "81^1mnfa.,1&adFra1*13T1maul/1dADmb" in pwd
        and "X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz" in pwd
    ):
        key = [
            ">",
            "*",
            "K",
            "Y",
            "W",
            "?",
            "1",
            "%",
            "$",
            " ",
            "8",
            "s",
            "k",
            "=",
            "`",
            "M",
            ";",
            "\\",
            "2",
            "/",
            "4",
            "b",
            "B",
            "~",
            "&",
            "c",
            "3",
            ":",
            "<",
            "h",
            "L",
            "v",
            "j",
            "l",
            ".",
            "|",
            '"',
            "n",
            "P",
            "F",
            "_",
            "C",
            "G",
            "^",
            "Q",
            "(",
            "z",
            "6",
            "o",
            "r",
            "q",
            "D",
            "g",
            "X",
            "y",
            "]",
            "i",
            "}",
            "u",
            "p",
            "t",
            "{",
            "[",
            "!",
            "0",
            "x",
            "A",
            "J",
            "T",
            "+",
            "w",
            "a",
            "'",
            "#",
            "@",
            "Z",
            "m",
            "N",
            "V",
            "7",
            "R",
            ")",
            "O",
            "d",
            "9",
            "S",
            "E",
            "f",
            "-",
            ",",
            "H",
            "e",
            "U",
            "I",
            "5",
        ]

        pwd = pwd.replace("X3b$uE5vP9sA1rZ2wC4mH6nT8gF7jL0qKtOyDz", "")
        pwd = pwd.replace("81^1mnfa.,1&adFra1*13T1maul/1dADmb", "")

        for letter in pwd:
            index = key.index(letter)
            pwd_new += chars[index]

        name_new = "".join(name_new)
        pwd_new = "".join(pwd_new)

    return web, name_new, pwd_new


def file(web, name, pwd):
    passwords = open("passwords.txt", "a")
    passwords.write("\n")
    passwords.write(f"{web}0000000{name}0000000{pwd}")
    passwords.close()


while 1:
    add_get = input(
        "Do you want to add a new password or get an existing one (a or r)? "
    )
    if add_get == "a":
        new_old = input(
            "Do you want to generate a new password or use an existing one (n or o)? "
        )
        if new_old == "o":
            web = input("Enter the name of the website: ")
            name = input("Enter the username: ")
            pwd = input("Enter the password: ")
            web, name, pwd = encrypter(web, name, pwd)
            file(web, name, pwd)
        elif new_old == "n":
            web = input("Enter the name of the website: ")
            name = input("Enter the username: ")
            n = input("Enter the length of the password: ")

            pwd = generate_password(int(n))
            print(f"Your password is {pwd}")

            web, name, pwd = encrypter(web, name, pwd)
            file(web, name, pwd)
    elif add_get == "r":
        which = input("What website do you want to get access to? ")
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if which in line:
                    web, name, pwd = decrypt(line)
                    print(f"{web} = {name} : {pwd}")

    else:
        print("Invalid input")
        continue
