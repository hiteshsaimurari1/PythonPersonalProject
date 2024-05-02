from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timex = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timex)
    canvas.itemconfig(text_line, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text=" ")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_line():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg="#e7305b")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg="#e7305b")
    else:
        count_down(work_sec)
        timer.config(text="Work Time", fg="#9bdeac")



def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_line, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timex
        timex = window.after(3, count_down, count-1)
    else:
        start_line()
        marks = " "
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        checkmark.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME,50,"bold"), bg=YELLOW)
timer.grid(row=0, column=1)

start_button = Button(text="Start", command=start_line)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=3, column=3)

checkmark = Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME,15,"bold"))
checkmark.grid(row=4,column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
text_line = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)





window.mainloop()