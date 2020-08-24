import turtle
import random
import time


def forward(z):
    return z.forward(random.randint(1, 6))  # Chooses a random distance the turtles will travel


turtle.setworldcoordinates(0, 0, 100, 100)  # Size of their world

still_going = True  # Variable for checking if they are still racing

score = [0, 0, 0, 0, 0]  # Score table for each of the five turtles

while still_going:          # While loop that checks if a turtle made it to 3 wins

    # Initiate the turtles
    turtle_1 = turtle.Turtle()
    turtle_2 = turtle.Turtle()
    turtle_3 = turtle.Turtle()
    turtle_4 = turtle.Turtle()
    turtle_5 = turtle.Turtle()

    # Color the turtles
    turtle_1.color('red')
    turtle_2.color('blue')
    turtle_3.color('green')
    turtle_4.color('grey')
    turtle_5.color('purple')

    # Make a list so we can iterate over and change for each one
    lst = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5]

    # Make the speed to max and lift pen so they don't make lines while going to start position
    for tur in lst:
        tur.speed(0)
        tur.penup()

    # Make the turtles go to their start position
    turtle_1.setpos(10, 0)
    turtle_2.setpos(30, 0)
    turtle_3.setpos(50, 0)
    turtle_4.setx(70)
    turtle_5.setx(90)

    # Down with pen and make them face up towards the goal
    for tur in lst:
        tur.pendown()
        tur.left(90)

    # Make the speed to 5
    for tur in lst:
        tur.speed(5)

    # While loop for making the turtles race until at least one reaches the goal
    while turtle_1.pos() < (10, 100) and turtle_2.pos() < (30, 100) and turtle_3.pos() < (50, 100) and \
            turtle_4.pos() < (70, 100) and turtle_5.pos() < (90, 100):
        for tur in lst:
            tur.forward(random.randint(1, 6))

    # Gives 1 point to the turtle that reached the goal,
    # if there are more than one that reaches the goal at the same time,
    # then all the turtles that reaches the goal get points
    for x in range(5):
        if lst[x].ycor() >= 100:
            score[x] += 1


    print(score)
    for x in range(5):
        if score[x] >= 3:
            still_going = False
            turtle.clearscreen()
            turtle.Turtle()
            turtle.goto(30, 50)
            # turtle.textinput('Turtle{} finished'.format(x+1), 'Turtle{} finished the race'.format(x+1))
            turtle.write('Turtle {} finished'.format(x+1), True, align='center', font=('Timesnewroman', 30, 'bold italic'))
            time.sleep(2)
    time.sleep(2)
    turtle.clearscreen()
