from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbol + password_letter

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't let any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                  f"Email: {email}\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.text", "a") as data_file:
                data_file.write(f"{website}  |  {email}  |  {password}\n")
                website_input.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

website = Label(text="Website:")
website.grid(column=1, row=2)
email = Label(text="Email/Username:")
email.grid(column=1, row=3)
password_ = Label(text="Password:")
password_.grid(column=1, row=4)

website_input = Entry(width=35)
website_input.grid(column=2, row=2, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(0, "agave030@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=2, row=4)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=3, row=4)
add = Button(text="Add", width=36, command=save)
add.grid(column=2, row=5, columnspan=3)

window.mainloop()
