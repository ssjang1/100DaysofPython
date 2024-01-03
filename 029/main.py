from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_info = website_entry.get()
    email_username_info = email_username_entry.get()
    password_info = password_entry.get()
    # f = open('./029/data.txt','a')
    # f.write(f'{website_info}, {email_username_info}, {password_info}\n')
    # f.close()
    
    if len(website_info) ==0 or len(password_info)==0:
        messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty")
    
    is_ok = messagebox.askokcancel(title=website_info, message=f'These are the details enterd: \nEmail:{email_username_info}\n Password:{password_info} \nIs it ok to save?')
    
    if is_ok:
        with open('./029/data.txt','a') as f:
            f.write(f'{website_info}, {email_username_info}, {password_info}\n')
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            # email_username_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='./029/logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1,row=1)

# Label
website_label = Label(text='Website')
email_username_label = Label(text='Email/Username')
password_label = Label(text='Password')

website_label.grid(column=0,row=2)
email_username_label.grid(column=0,row=3)
password_label.grid(column=0, row=4)
# Entry

website_entry = Entry(width=42)
email_username_entry = Entry(width=42)
password_entry = Entry(width=26)

website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()

email_username_entry.grid(column=1, row=3,columnspan=2)
email_username_entry.insert(0, 'example@example.com')
password_entry.grid(column=1, row=4)



# Button
generate_button = Button(text='Generate Password',command=generate_password)
add_button = Button(text='Add',width=41, command=save)

generate_button.grid(column=2, row=4)
add_button.grid(column=1,row=5,columnspan=2)
window.mainloop()