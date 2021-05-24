from tkinter import *
import random
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# -----------------------------Pandas-----------------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")   # dataframe
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
# -----------------------------Function------------------------------
def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(languages, text="French", fill="black")
    canvas.itemconfig(words, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_png)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(languages, text="English", fill="white")
    canvas.itemconfig(words, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_png)

def is_known():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()

# --------------------------------UI------------------------------
# Creating window
window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Creating image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_png = PhotoImage(file="images/card_front.png")
card_back_png = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_png)
canvas.grid(column=1, row=1, columnspan=2)

# Creating button and image
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=2, row=2)
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=generate_word)
wrong_button.grid(column=1, row=2)

# Creating word
words = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
languages = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

generate_word()

window.mainloop()