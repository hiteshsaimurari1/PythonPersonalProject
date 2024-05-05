from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = ([random.choice(letters) for char in range(nr_letters)]
                     + [random.choice(symbols) for char in range(nr_symbols)]
                     + [random.choice(numbers) for char in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_enter.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_command():
    website_c = website_enter.get()
    email_c = email_enter.get()
    password_c = password_enter.get()

    if len(website_c) == 0 or len(password_c) == 0:
        messagebox.showinfo(title="Warning", message="Enter the website properly")
    else:
        Is_ok = messagebox.askyesno(title=website_c, message=f"These are the  details entered:\n Email:{email_c} \n "
                                                             f"Password:{password_c} \n Is it ok to save?")
        if Is_ok:
            inp = f"{website_c} | {email_c} | {password_c}\n"
            f = open("data.txt", "a")
            f.write(inp)
            website_enter.delete(0, END)
            password_enter.delete(0, END)
            website_enter.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)



website = Label(text="Website:")
website.grid(row=1,column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

website_enter = Entry(width=35)
website_enter.grid(row=1, column=1, columnspan=2)
email_enter = Entry(width=35)
email_enter.insert(0,"hitesh@email.com")
email_enter.grid(row=2, column=1, columnspan=2)
password_enter = Entry(width=21)

password_enter.grid(row=3, column=1)

generate = Button(text="Generate Password", command=generator)
generate.grid(row=3, column=2)

add = Button(text="Add", width=36, command=add_command)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()