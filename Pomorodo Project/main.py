from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
checks = "✔"
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global checks
    global timer
    global reps
    checks = "✔"
    checkmark.config(text='')
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # work_sec = 5
    # short_break_sec = 5
    # long_break_sec = 5

    if reps % 4 == 0:
        countdown(long_break_sec)
        heading.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        countdown(work_sec)
        heading.config(text="Work", fg=GREEN)
    else:
        countdown(short_break_sec)
        heading.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global checks
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark.config(text=checks)
            checks += "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomorodo Work Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
heading.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
