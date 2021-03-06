from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
CHECK = "✓"
repetitions = 0
timer = None


def reset_timer():
    """ this function resets timer by configuring clock label and setting repetitions to 0"""
    window.after_cancel(timer)
    global repetitions
    repetitions = 0
    LABEL.config(text="TAJMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 44, "bold"))
    canvas.itemconfig(timer_text, text="00:00")


def start_timer():
    """this function checks number of repetitions and displays different countdowns depending on repetition number.
    Every other repetition is a short break, and every 8th repetition is long break. Odd number of repetitions means that work minuts should be counted
    Every two repetitions is full cycle, so a check mark is added at the bottom of the screen"""
    global repetitions
    global LABEL
    global check
    global CHECK
    repetitions += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        count_down(long_break_sec)
        LABEL.config(text="PAUZA", fg=RED)
        check.config(text=CHECK * (repetitions // 2), )
    elif repetitions % 2 == 0:
        count_down(short_break_sec)
        LABEL.config(text="PAUZA", fg=PINK)
        check.config(text=CHECK * (repetitions // 2), )
    else:
        count_down(work_sec)
        LABEL.config(text="RADI!", fg=GREEN)


def count_down(count):
    """this function configures canvas every 1000 millisecond and displays minutes and seconds left to the end of repetition cycle"""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

#game engine and UI   
if __name__ == "__main__":
    window = Tk()
    window.title("Pomorodo timer")
    window.config(padx=100, pady=50, bg=YELLOW)

    tomato = PhotoImage(file="tomato.png")

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    canvas.create_image(100, 112, image=tomato)
    canvas.grid(row=1, column=1)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="yellow", font=(FONT_NAME, 35, "bold"))

    LABEL = Label(text="TAJMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 44, "bold"))
    LABEL.grid(row=0, column=1)

    START_BUTTON = Button(text="POČNI", command=start_timer)
    START_BUTTON.grid(row=2, column=0)

    RESET_BUTTON = Button(text="PONOVI", command=reset_timer)
    RESET_BUTTON.grid(row=2, column=2)

    check = Label(text=" ", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
    check.grid(row=3, column=1)

 

    window.mainloop()
