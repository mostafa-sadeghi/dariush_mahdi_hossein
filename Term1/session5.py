a = 4
b = 5

# if a >= b:
#     print("a is greater than b")
#     print("ballalalal")
# else:
#     print("b is greater than a")
#
# print("outSide")


# if a == b:
#     print("a and b are equal")
# else:
#     print("a and b are not equal")

#
# if a != b:
#     print("a and b are not equal")
# else:
#     print("a and b are equal")


# number1 = float(input("Enter a number: "))
# number2 = float(input("Enter a number: "))
#
# if number1 > number2:
#     print(f"number1 : {number1} is greater than number2 :{number2}")
#
# elif number1 < number2:
#     print(f"number2 : {number2} is greater than number1 :{number1}")
# else:
#     print(f"number1 : {number1} is equal to number2 :{number2}")


# number1 = float(input("Enter a number: "))
# number2 = float(input("Enter a number: "))
# number3 = float(input("Enter a number: "))
#
# if number1 > number2 and number1 > number3:
#     print(f"max is {number1}")
# elif number2 > number1 and number2 > number3:
#     print(f"max is {number2}")
# else:
#     print(f"max is {number3}")
#
# print("max is", max(number1, number2, number3))

#
# user_name = input("Enter the username: ")
# if user_name == "sara" or user_name == "artin":
#     print(f"{user_name} is valid.")
# else:
#     print(f"{user_name} is not valid")


# a = False
# if not a:
#     print("ok")


# TODO
"""
برنامه ای بنویسید که نام و نمرات سه درس یک دانش آموز را از ورودی دریافت نماید
و سپس معدل وی را حساب نماید
و در نهایت اگر معدل او را نوزده بیشتر بود
A
را پرینت نماید
اگر معدل او از هجده بیشتر بود 
B
را پر ینت نماید

اگر معدل او از هفده بیشتر بود
C
را پرینت نماید

اگر معدل او از شانزده بیشتر بود 
D
را پرینت نماید
در غیر اینصورت 
E
را پرینت نماید

"""

user_name = input("Enter your username: ")
password = input("Enter your password: ")

if user_name == "admin" and password == "123":
    print(f"{user_name} is valid")
else:
    print(f"{user_name} is not valid")