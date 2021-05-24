import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

states = pd.read_csv("50_states.csv")
state_list = states.state.to_list()
x_list = states.x.to_list()
y_list = states.y.to_list()
correct_guess = []
scores = 0
still_continue = True

while still_continue:
    if scores == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another states name?").title()
    elif scores <= 50:
        answer_state = screen.textinput(title=f"{scores}/50 States Correct",
                                        prompt="What's another states name?").title()
    else:
        still_continue = False
    if answer_state == "Exit":
        missing_state = [state for state in state_list if state not in correct_guess]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv()
        break
    for states_name in state_list:
        if answer_state == states_name:
            pen.goto(x_list[state_list.index(states_name)], y_list[state_list.index(states_name)])
            pen.write(states_name, False, font=("Arial", 10, "normal"))
            correct_guess.append(answer_state)
            scores += 1

"""
Another way:
if answer_state in state_lists:
    t = turtle.Turtle()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x, state_data.y)
    t.write(answer_state)
"""