from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn_words = []

try:
    dt = pd.read_csv("data/words_to_learn.csv")
    to_learn = dt.to_dict(orient="records")


except FileNotFoundError:
    dt = pd.read_csv("data/french_words.csv")
    to_learn = dt.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    card_canvas.itemconfig(card_word, text=f"{current_card['French']}", font=("Arial", 60, "bold"))
    card_canvas.itemconfig(canvas_image, image=front_image)
    card_canvas.itemconfig(card_word, fill="black")
    card_canvas.itemconfig(card_title, fill="black")
    flip_timer = window.after(3000, func=change_image)


def change_image():
    card_canvas.itemconfig(canvas_image, image=back_image)
    card_canvas.itemconfig(card_title, fill="white", text="English")
    card_canvas.itemconfig(card_word, fill="white", text=current_card["English"])


def is_kwown():
    global learn_words
    to_learn.remove(current_card)
    new_dict = pd.DataFrame.from_dict(to_learn)
    new_dict.to_csv("data/words_to_learn")
    next_card()


#  --------------- UI ---------------
# Window


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
flip_timer = window.after(3000, change_image)

# White Card

card_canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card_canvas.create_image(400, 263, image=front_image)
card_title = card_canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = card_canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2, sticky="EW", padx=10, pady=10)

# Wrong Button

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Correct Button

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, command=is_kwown)
correct_button.grid(row=1, column=1)

next_card()
window.mainloop()
