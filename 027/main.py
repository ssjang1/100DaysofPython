import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width= 500, height= 300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text ='I am a Label',font=('Arial', 24, "bold"))
my_label.pack()

my_label['text'] = 'New Text1'
my_label.config(text='New Text2')
# my_label.place(x=100,y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Button

def button_clicked():
    # print('I got clicked')
    # my_label.config(text ='i got clicked~')
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text ='Click Me', command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text='new_button')
new_button.grid(column=2, row=0)

#Entry


    
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3,row=2)


window.mainloop()