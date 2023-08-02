# name = input("enter student's name: ")
# score1 = float(input("enter student's score: "))
# score2 = float(input("enter student's score: "))
# score3 = float(input("enter student's score: "))

# total = score1 + score2 + score3
# ave = total/3
# print(f"{name}'s average is : {ave:.2f}")
# if ave >= 19:
#     print(f"{name}'s grade is A")
# elif ave >= 18:
#     print(f"{name}'s grade is B")
# elif ave >= 17:
#     print(f"{name}'s grade is C")
# elif ave >= 16:
#     print(f"{name}'s grade is D")
# elif ave >= 15:
#     print(f"{name}'s grade is E")
# else:
#     print(f"{name}'s grade is F")

# for i in range(10):
#     print("hi")


# for i in range(10):
#     print(i)

# for i in range(1, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i, end=" ")
# print()
# for i in range(10, 0, -1):
#     print(i, end=" ")
# print()
# for i in range(10, -1, -1):
#     print(i, end=" ")


# for number in [1, 2, 3, 3, 4, 4, 5, 5, 5]:
#     print(number)

# TODO  با کمک حلقه فور اعداد زوج 2 تا 20 را پرینت نمائید


# TODO
"""
برنامه ای بنویسید که با کمک حلقه فور
پنج عدد از ورودی دریافت نماید و حاصل جمع اعداد فرد را محاسبه نماید
عدد فرد عددی است که باقیمانده تقسیم ان بر دو مساوی صفر نیست

"""


"""
لا کمک  حلقه فور، برنامه ای بنویسید که نام پنج دانش آموز را از ورودی دریافت نماید
و در لیتی ذخیره کند



"""


"""

با کمک حلقه فور برنامه ای بنویسید که نام و سن پنج دانش آموز را از ورودی دریافت نماید و 
برای هر دانش آموز یک دیکشنری بساز د و هر دیکشنری را درون لیست اضافه نماید.

"""

import turtle
screen = turtle.Screen()

my_turtle = turtle.Turtle()
my_turtle.color("red")
my_turtle.pensize(4)

sides = int(screen.textinput("userinput", "How many sides? "))

for i in range(sides):
    my_turtle.forward(100)
    my_turtle.left(360/sides)


turtle.done()


# TODO
"""
با کمک حلقه فور برنامه ای بنویسید که یک ستاره بکشد
"""


# # TODO
numbers = [1, 2, 4, 6, 88, 99, 90]
""""
با کمک حلقه فور ، مجموع اعداد لیست بالا را محاسبه نمایید
و حاصل جمع را نمایش دهید
"""
