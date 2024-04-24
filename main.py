import turtle as tur
import pandas as pd

screen = tur.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tur.shape(image)

# Load state data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = [ ]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct ",
                                    prompt="What is the name of another state?").title()

    if answer_state is None or answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_state_csv = pd.DataFrame(missing_states, columns=[ 'state' ])
        missing_state_csv.to_csv("Missing_state.csv", index=False)
        break# Exit the loop if user cancels the input dialog

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = tur.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data [ data.state == answer_state ]
        #t.goto(int(state_data.x), int(state_data.y))
        t.goto(int(state_data.iloc [ 0 ] [ 'x' ]), int(state_data.iloc [ 0 ] [ 'y' ]))
        t.write(state_data.state.item())

new_csv = pd.DataFrame(guessed_states, columns=['state'])
new_csv.to_csv("Correct_Guessed_list.csv", index=False)
# Close the screen properly
screen.mainloop()






