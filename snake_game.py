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
    object.goto(x, y)


snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def reset(snake_tails):
    snake_head.home()
    global score
    score = 0
    snake_head.direction = ""
    for tail in snake_tails:
        tail.ht()

    snake_tails = []


main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_right, "Right")
main_surface.onkeypress(go_left, "Left")
main_surface.tracer(False)
snake_tails = []
score = 0
my_turtle = create_turtle("square", "white")
my_turtle.goto(0, 260)
my_turtle.ht()

running = True
while running:
    my_turtle.clear()
    my_turtle.write(f"Score: {score}", font=("arial", 22), align="center")

    main_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        new_tail = create_turtle("square", "green")
        snake_tails.append(new_tail)
        score += 1

    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i-1].xcor()
        y = snake_tails[i-1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 230 or snake_head.ycor() < -290:
        reset(snake_tails)

    move_snake()
    for t in snake_tails:
        if snake_head.distance(t) < 20:
            reset(snake_tails)

    sleep(0.2)
