from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
PURPLE= "#DFD3C3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps%8 == 0:
        label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        countdown(long_break_sec)

    elif reps % 2 == 0:
        label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        countdown(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canva.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, countdown,count-1)
    else:
        start_timer()
        mark = ""

        for i in range(math.floor(reps/2)):
            mark+="✓"
        check_mark.config(text = mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=50,pady=50,bg=YELLOW)

canva = Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canva.create_image(100,112,image=tomato_image)
timer_text = canva.create_text(100,130,text="00:00",fill = "white",font=(FONT_NAME,20,"bold"))
canva.grid(column=1,row=1)

label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
label.grid(column = 1,row =0)

start = Button(text="Start",width=10,command=start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",width=10,command=reset_timer)
reset.grid(column=2, row=2)

check_mark=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check_mark.grid(column=1,row=3)


window.mainloop()