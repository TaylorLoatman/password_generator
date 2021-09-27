from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gernerate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
  password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
  password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

  password_list = password_letters + password_number + password_symbols

  random.shuffle(password_list)

  password = "".join(password_list)
  password_input.insert(0, password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

  website = website_input.get()
  user = email_input.get()
  password = password_input.get()

  if len(user) == 0 or len(password) == 0:
    messagebox.showinfo(title="Ooops", message="OH NO! Please make sure all fields are filled in.")
  else:

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {user} "
                                                  f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:
      with open("pw_keeper.txt", "a") as file:
        file.write(f"{website} | {user} | {password}\n")

      website_input.delete(0, END)
      password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pw_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_img)
canvas.grid(column=1, row=0)

#Website Entrt
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.get()
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

#Email Entry
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.get()
email_input.insert(0, "tester@test.com")
email_input.grid(column=1, row=2, columnspan=2)

#Password Genorator
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.get()
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=gernerate_password)
generate_button.grid(column=2, row=3)

#Copy to Clipboard Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
