import random
import turtle

screen = turtle.Screen()
screen.setup(height=400, width=500)

colours = ['red', 'blue', 'black', 'green', 'yellow', 'orange']
y_axis = [150, 90, 30, -30, -90, -150]
user_bet = screen.textinput(title="Turtle race bet", prompt="In which color Turtle you are betting?\n Red, Blue, "
           
                                                            "Black, Green, Yellow, Orange").lower()
end_line = turtle.Turtle()
end_line.hideturtle()
end_line.color("black")
end_line.penup()
end_line.goto(230, 200)
end_line.pendown()
end_line.right(90)
end_line.goto(230, -200)

turtles = []
result_dict = {
    "red": 0,
    "blue": 0,
    "black": 0,
    "green": 0,
    "yellow": 0,
    "orange": 0,
}
for i in range(0, 6):
    turtl = turtle.Turtle()
    turtl.penup()
    turtl.shape('turtle')
    turtl.color(colours[i])
    turtl.goto(-230, y_axis[i])
    turtles.append(turtl)

race_range = 0
winner = None
while race_range < 230:
    for i in range(6):
        rand_step = random.randint(0, 10)
        turtles[i].forward(rand_step)
        if turtles[i].xcor() > race_range:
            race_range = turtles[i].xcor()
            winner = i

print(user_bet)
if user_bet == colours[winner]:
    print(f"You Won!, the winner is {colours[winner].title()}")
    screen.textinput(title="Result !", prompt=f"You WON!,\nThe winner is '{colours[winner].upper()}'\npress 'ENTER'")
else:
    print(f"You Lose!, the winner is {colours[winner].title()}")
    screen.textinput(title="Result !", prompt=f"You Lose!,\nThe winner is '{colours[winner].upper()}'\npress 'ENTER'")

screen.exitonclick()
