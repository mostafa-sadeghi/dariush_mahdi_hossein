import turtle

main_screen = turtle.Screen()
main_screen.bgcolor("orange")
# main_screen.bgpic("clown.png")
#  نکته برای اضافه کردن تصویر پس زمینه حتما باید از عکس با پسوند png استفاده نمائید
# برای اضافه کردن عکس برای ترتل باید از عکس با پسوند gif استفاده نمائید
main_screen.register_shape("strawberry.gif")
my_turtle = turtle.Turtle()
# my_turtle.shape("turtle")
my_turtle.shape("strawberry.gif")
my_turtle.shapesize(4)
my_turtle.pensize(4)
my_turtle.color("red")

# my_turtle.forward(200)
# my_turtle.stamp()
# my_turtle.left(120)
#
#
# my_turtle.forward(200)
# my_turtle.stamp()
#
# my_turtle.left(120)
#
# my_turtle.forward(200)
# my_turtle.stamp()

my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()
# TODO
"""
کشیدن مربع
کشیدن پنج ضلعی
کشیدن شش ضلعی

"""

turtle.done()