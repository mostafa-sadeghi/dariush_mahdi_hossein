# def get_cost_coffee(number_of_coffees, price_per_coffee):
#     free_coffees = number_of_coffees // 9
#     paid_coffees = number_of_coffees - free_coffees
#     return paid_coffees * price_per_coffee


# print(get_cost_coffee(7, 2.5))  # 17.5
# print(get_cost_coffee(8, 2.5))  # 20
# print(get_cost_coffee(9, 2.5))  # 20
# print(get_cost_coffee(10, 2.5))  # 22.5

import random
import string
LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
DIGITS = string.digits
PUNC = "~!@#$%^&*()_+"
ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + DIGITS + PUNC

def create_password(length):
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
    return "".join(password)

print(create_password(5))



