import random
import string
import pyperclip
LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
DIGITS = string.digits
PUNC = "!@#"
ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + DIGITS + PUNC


def create_password(site, length):
    if length < 12:
        length = 12
    password = []
    password.append(random.choice(LOWER_LETTERS))
    password.append(random.choice(UPPER_LETTERS))
    password.append(random.choice(DIGITS))
    password.append(random.choice(PUNC))

    while len(password) < length:
        password.append(random.choice(ALL_CHARS))

    random.shuffle(password)
    password = "".join(password)
    pyperclip.copy(password)

    my_file = open(site+".txt", "w")
    my_file.write(password)
    my_file.close()
    return password


site_name = input("Enter site's name: ")
password_length = int(input("enter the password length: "))

create_password(site_name, password_length)
