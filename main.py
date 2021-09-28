from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
  new_data = {
    website: {
      "email": user,
      "password": password
    }
  }

  if len(user) == 0 or len(password) == 0:
    messagebox.showinfo(title="Ooops", message="OH NO! Please make sure all fields are filled in.")
  else:
    try:
      with open("pw_keeper.json", "r") as file:
        #Reading old data
        data = json.load(file)

    except FileNotFoundError:
      with open("pw_keeper.json", "w") as file:
        #Save updated data
        json.dump(data, file, indent=4)
    else:
      # Updating old datye with new data
      data.update(new_data)

      with open("pw_keeper.json", "w") as file:
        #Save updated data
        json.dump(data, file, indent=4)
    finally:
      website_input.delete(0, END)
      password_input.delete(0, END)

# ---------------------------- Find Password ------------------------------- #

def find_password():
  website = website_input.get()
  try:
    with open("pw_keeper.json") as file:
      data = json.load(file)
  except FileNotFoundError:
      messagebox.showinfo(title="Oh No!", message="No Data File Found")
  else:
      if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
      else:
        messagebox.showinfo(title="Website Not Found", message=f"No details for the {website} exists.")

  finally:
    file.close()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pw_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_img)
canvas.grid(column=1, row=0)

#Website Entry
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.get()
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)



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

gernerate_button = Button(text="Generate Password", command=gernerate_password)
gernerate_button.grid(column=2, row=3)

#Copy to Clipboard Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
