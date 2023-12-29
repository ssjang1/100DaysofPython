import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title('U.S. States Game')

image= './025/us-states-game-start/us-states-game-start/blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv('./025/us-states-game-start/us-states-game-start/50_states.csv')

guessed_states = []

while len(guessed_states) <50:
    answer_state = screen.textinput(title='Guess the State', prompt='What is another state name')
    all_states = data['state'].to_list()

    if answer_state in all_states:
        guessed_states.apppend(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data['x']),int(state_data['y']))
        t.write(state_data.state.item())

# def get_mouse_click_coor(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

screen.exitonclick()