from colorama import Fore,Back,Style,init
import random
import string
init()
Num_of_digits = 3
Max_guess = 10
print(f"""{Fore.RED}Welcome to my game.{Style.RESET_ALL}
{Back.MAGENTA}You must guess {Num_of_digits} digits number.{Style.RESET_ALL}
{Back.GREEN}You have {Max_guess} times to guess it.{Style.RESET_ALL}
""")

def generate_secret_number():
    all_digits = list(string.digits)
    random.shuffle(all_digits)
    return "".join(all_digits[:3])

def verify_user_guess(user_g, sec_num):
    if user_g == sec_num:
        return "You Won!!!"
    hint = ""
    for i in range(Num_of_digits):
        if user_g[i] == sec_num[i]:
            hint += "Fermi, "
        elif user_g[i] in sec_num:
            hint += "Pico, "
    if len(hint) == 0:
        return "Bagels"
    return hint

while True:
    secret_number = generate_secret_number()
    print("secret number generated.")
    for i in range(Max_guess):
        print(f"Guess #{i+1}")
        user_guess = input(f"Enter {Num_of_digits} digits number: ")
        print(f"your guess is:{user_guess}")
        res = verify_user_guess(user_guess, secret_number)
        if res == "You Won!!!":
            print("You Won!!!")
            break
        print(res)
    if input("Do you want to continue? {y or n} ") == "n":
        print("Bye")
        break