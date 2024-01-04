BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

try: 
    french_words = pd.read_csv('./031/data/words_to_learn.csv')
except FileNotFoundError:
    french_words = pd.read_csv('./031/data/french_words.csv')
finally:
    french_dictionary = french_words.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dictionary)
    canvas.itemconfig(card_title, text='French',fill='black')
    canvas.itemconfig(card_word, text=current_card['French'],fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English',fill='white')
    canvas.itemconfig(card_word, text=current_card['English'],fill='white')
    canvas.itemconfig(card_background, image=card_back)
    
    
def is_known():
    french_dictionary.remove(current_card)
    next_card()
    data = pd.DataFrame(french_dictionary)
    data.to_csv('./031/data/words_to_learn.csv',index=False)
    print(len(data))
window =Tk()
window.title('flash card quiz')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

card_back = PhotoImage(file ='./031/images/card_back.png')
card_front = PhotoImage(file ='./031/images/card_front.png')
right = PhotoImage(file ='./031/images/right.png')
wrong = PhotoImage(file ='./031/images/wrong.png')

canvas= Canvas(width=800, height=526)

card_background = canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150, text='Title',font=('Arial',40,'italic'))
card_word = canvas.create_text(400,263, text='word', font=('Arial',60,'bold'))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)

right_button = Button(image=right, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)

right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()