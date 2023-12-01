from state import State
import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(800, 550)

state = State()
game_is_on = True
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while game_is_on:
    input_value = screen.textinput(title=f"{state.score}/50 ~ Guess the State", prompt="What's another state's name?").title()

    while input_value in state.states:
        input_value = screen.textinput(title="Guess the State", prompt="This state written before. Guess another state.").title()

    state_values = (data[data["state"] == input_value])
    if input_value == "Exit":
        missing_states = []
        for new_state in all_states:
            if new_state not in state.states:
                missing_states.append(new_state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        break

    if (state_values.state == False).all():
        state.wrong_answer()
        game_is_on = False
        break

    state.create_state(input_value.capitalize(), int(state_values.x), int(state_values.y))
    state.increase_score()

screen.exitonclick()
