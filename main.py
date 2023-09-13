import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. State Game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# Read data
data = pandas.read_csv("50_states.csv")
screen.tracer(0)
turtle.penup()
correct_answer = []
# Set up the scoreboard
scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-80, 250)
scoreboard.write(f"{len(correct_answer)}/{len(data.state)}", align="center", font=("Courier", 8, "normal"))
# Main game loop
while len(correct_answer) < len(data.state):
    time.sleep(0.1)
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name").title()
    if answer_state == "Exit":
        break

    current_state = data[data["state"] == answer_state]
    if not current_state.empty and answer_state not in correct_answer:
        # Update the scoreboard
        scoreboard.clear()
        scoreboard.write(f"{len(correct_answer)}/{len(data.state)}",
                         align="center", font=("Courier", 8, "normal"))
        # Display the guessed state on the map
        x_cor = int(data[data.state == answer_state].x.item())
        y_cor = int(data[data.state == answer_state].y.item())
        turtle.goto(x_cor, y_cor)
        turtle.write(f"{answer_state}", align="center", font=("Courier", 8, "normal"))
        turtle.goto(0, 0)
        correct_answer.append(answer_state)
    else:
        continue  # Incorrect answer, continue the loop
screen.exitonclick()
