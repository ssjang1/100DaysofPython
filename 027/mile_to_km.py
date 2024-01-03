import tkinter
window = tkinter.Tk()
window.title('Mile to Km Converter')
# window.minsize(width= 500, height= 300)
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km = round(km,2)
    kilometer_result_label.config(text=km)


miles_input = tkinter.Entry()
miles_input.grid(column= 1, row=0)


miles_label = tkinter.Label(text ='Miles')
is_equal_label = tkinter.Label(text ='is equal to')
kilometer_result_label = tkinter.Label(text ='0')
kilometer_label = tkinter.Label(text ='Km')

calculate_button = tkinter.Button(text='Calculate',command=miles_to_km)
calculate_button.grid(column=1, row=2)

miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
kilometer_result_label.grid(column=1, row=1)
kilometer_label.grid(column=2, row=1)



window.mainloop()