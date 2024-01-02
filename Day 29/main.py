from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL_CHARACTER = "!'^+%&/()=?_<>|#${[]}"
CHARACTERS = [LOWERCASE_LETTERS, UPPERCASE_LETTERS, DIGITS, SPECIAL_CHARACTER]


def generate_password():
    password = ""
    password_entry.delete(0, END)
    for _ in range(16):
        characters = random.choice(CHARACTERS)
        character = random.choice(characters)
        password += character
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def read_data():
    if website_entry.get() == "" or password_entry.get() == "" or mail_username_entry.get() == "":
        messagebox.showwarning("Warning", "You should fill the all blank before the save")
    else:
        if messagebox.askokcancel(title="Warning", message="Are you sure you want this information to be saved?"):
            with open("data.txt", "a") as file:
                file.write(f"{website_entry.get()} | {mail_username_entry.get()} | {password_entry.get()}\n")
            messagebox.showinfo(title="Info", message="Adding is successful")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            mail_username_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# Website Label

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Website Entry

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW"),
website_entry.focus()

# Email/Username Label
mail_username_label = Label(text="Email/Username:")
mail_username_label.grid(row=2, column=0)

# Email/Username Entry

mail_username_entry = Entry(width=35)
mail_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
mail_username_entry.insert(0, "emihansagol@sagol.com")

# Password Label

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Password Entry

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=2, sticky="EW")

# Generate Password Button

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2, sticky="EW")

# Add Button

add_button = Button(text="Add", width=36, command=read_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

# Image

canvas = Canvas(highlightthickness=0, height=200, width=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

window.mainloop()
