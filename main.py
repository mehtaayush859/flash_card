from tkinter import *
import pandas
import random

FONT = ("Ariel", 40, "italic")
NEXT_FONT = ("Ariel", 60, "bold")
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_dict = {}

try:
    data = pandas.read_csv("D:/Courses_tele/Practical/Flash_card_project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("D:/Courses_tele/Practical/Flash_card_project/data/french_words.csv")
    to_learn_dict = original_data.to_dict(orient="records")
else:
    to_learn_dict = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(4000, func=flip_card)

def is_known():
    to_learn_dict.remove(current_card)
    data = pandas.DataFrame(to_learn_dict)
    data.to_csv("D:\Courses_tele\Practical\Flash_card_project\data\words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, func=flip_card)
canvas = Canvas(height=526, width=800)
card_back_img = PhotoImage(file="D:/Courses_tele/Practical/Flash_card_project/images/card_back.png")
card_front_img = PhotoImage(file="D:/Courses_tele/Practical/Flash_card_project/images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=FONT)
card_word = canvas.create_text(400, 263, text="", font=NEXT_FONT)


wrong_img = PhotoImage(file="D:/Courses_tele/Practical/Flash_card_project/images/wrong.png")
wrong_but = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_but.grid(column=0, row=1)

right_img = PhotoImage(file="D:/Courses_tele/Practical/Flash_card_project/images/right.png")
right_but = Button(image=right_img, highlightthickness=0, command=is_known)
right_but.grid(column=1, row=1)


next_card()

window.mainloop()


