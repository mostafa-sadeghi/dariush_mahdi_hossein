import turtle

# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)




i = 0
while i < 4:
    turtle.forward(100)
    turtle.left(90)
    i += 1




while True:
    user_choice = input("Do you want to continue?(y or n) ")
    if user_choice == "n":
        break
