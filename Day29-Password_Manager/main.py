from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()
    password = password_entry.get()



    try:
        with open("passwords.json", mode="r") as pw_file:
            #Reading old data
            data = json.load(pw_file)
    except FileNotFoundError:
        messagebox.showinfo(message=f"No data file!")
    else:
        if website in data:
            messagebox.showinfo(message=f"Website: {website}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(message=f"No information for that website")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(letters) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Do not leave Website/Password field empty!")
    else:
        try:
            with open("passwords.json", mode="r") as pw_file:
                #Reading old data
                data = json.load(pw_file)
        except FileNotFoundError:
            with open("passwords.json", mode="w") as pw_file:
                json.dump(new_data, pw_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("passwords.json", mode="w") as pw_file:
                #Saving the updated data
                json.dump(data, pw_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


#Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#Website Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

#Search Button
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

#Username Label
username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)

#Username Entry
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "meehanc721@gmail.com")


#Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

#Generate Password Button
pw_button = Button(text="Generate Password", command=generate_password)
pw_button.grid(column=2, row=3, sticky="EW")

#Add Button
add_button = Button(text="Add", width=36, command=add_pw)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")



window.mainloop()