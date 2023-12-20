from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global reps
    reps = 0
    title.config(text="Timer", fg=GREEN, font=(FONT_NAME, 44, "bold"), bg=YELLOW)
    check_mark.config(text="", fg=GREEN, bg=YELLOW, font=("Arial", 12, "normal"))
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        reps = 0
        title.config(text="Long Break", fg=RED, font=(FONT_NAME, 32, "normal"))
        check_mark.config(text="✔" * (reps // 2))
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break", fg=PINK)
        check_mark.config(text="✔" * (reps // 2))
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = count // 60
    count_sec = count % 60

    if 0 <= count_sec < 10:
        count_sec = f"0{count_sec}"

    if 0 <= count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Title
title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 44, "bold"), bg=YELLOW)
title.grid(row=0, column=1)

# Reset Button

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

# Check Mark

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=("Arial", 12, "normal"))
check_mark.grid(row=3, column=1)

# Image

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start Button

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)


window.mainloop()
