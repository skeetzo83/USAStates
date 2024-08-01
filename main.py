import turtle
import pandas
from my_dot import Alona

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
alona = Alona()
data = pandas.read_csv("50_states.csv")
score = 0
guessed_states = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/{len(data)} Guess the State", prompt="What'the next state?").title()
    if answer_state in data.values:
        score += 1
        state_x = data.x[data.state == f"{answer_state}"].iloc[0]
        state_y = data.y[data.state == f"{answer_state}"].iloc[0]
        state_name = data.state[data.state == f"{answer_state}"].iloc[0]
        alona.correct(state_name, state_x, state_y)
        guessed_states.append(state_name)
    if answer_state == "Exit":
        missing_states = [state for state in data.state if state not in guessed_states]
        # for state in data.state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break

screen.exitonclick()
