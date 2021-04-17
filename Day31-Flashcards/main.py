from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    words = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_words = pandas.read_csv("data/french_words.csv")
    to_learn = original_words.to_dict(orient="records")
else:
    to_learn = words.to_dict(orient="records")

#------------------------------------------------Next Card--------------------------------------------------------------
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


#------------------------------------------------Flip Card--------------------------------------------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=current_word["English"])
    canvas.itemconfig(language_text, fill="white")
    canvas.itemconfig(word_text, fill="white")

#------------------------------------------------Known Card--------------------------------------------------------------
def is_known():
    to_learn.remove(current_word)
    #Save updated list
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    next_card()






window= Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# After 3 sec, flip card
flip_timer = window.after(3000, flip_card)

#Our canvas images to use
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")

#Makes the image the background
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

#Language text on canvas
language_text = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"))

#Word text on Canvas
word_text = canvas.create_text(400, 263, fill="black", font=("Arial", 60, "bold"))

#Right Button
right_image = PhotoImage(file="images/right.png")
correct_button = Button(image=right_image, highlightthickness=0, command=is_known)
correct_button.grid(column=1, row=1)

#Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()


window.mainloop()