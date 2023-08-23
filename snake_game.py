from random import randint
from turtle import Screen, Turtle
from time import sleep

main_surface = Screen()
main_surface.bgcolor("black")
main_surface.setup(600, 600)
main_surface.title("Snake Game")
def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle

def change_position(object):
    x = randint(-280, 280)
    y = randint(-280, 230)
    object.goto(x,y)

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

def go_up():
    snake_head.direction = "up"


# TODO برای سایر جهت ها 

main_surface.listen()
main_surface.onkeypress(go_up,"Up")

running = True
while running:
    main_surface.update()
    move_snake()
    sleep(0.2)



