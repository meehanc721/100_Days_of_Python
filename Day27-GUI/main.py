from tkinter import *


def button_clicked():
    answer = int(number.get()) * 1.609344
    converted = int(answer)
    label4.config(text=converted, font=("Arial", 14))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=50, height=40)

label1 = Label(text="                    ")
label1.grid(column=0, row=0)

# Entry
number = Entry(width=10)
number.focus()
number.grid(column=1, row=0)

# Label
label2 = Label(text="Miles", font=("Arial", 14))
label2.grid(column=2, row=0)

label3 = Label(text="is equal to", font=("Arial", 14))
label3.grid(column=0, row=1)

label4 = Label(text=" ", font=("Arial", 14))
label4.grid(column=1, row=1)

label5 = Label(text="Km", font=("Arial", 14))
label5.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
