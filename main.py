from tkinter import *
import math

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

def generate():
    print("Generating Password")

def add():
    print("Password Added")

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file = "logo.png")

logo_width = logo_img.width()
logo_height = logo_img.height()
print(f"width = {logo_width}, height = {logo_height}")
canvas.create_image(logo_width/2, logo_height/2, image=logo_img)
canvas.grid(column = 1, row = 0)
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)
website_entry = Entry(width = 35)
website_entry.grid(column = 1, row = 1, columnspan=2)
username_label = Label(text = "Email/Username:")
username_label.grid(column = 0, row = 2)
username_entry = Entry(width = 35)
username_entry.grid(column = 1, row = 2, columnspan=2)
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)
password_entry = Entry(width = 17)
password_entry.grid(column = 1, row = 3)
password_generator = Button(text = "Generate Password", command = generate)
password_generator.grid(column = 2, row = 3)
add_button = Button(text = "Add", command = add)
add_button.grid(column = 1, row = 4, columnspan = 2)


#user_width = math.floor(website_entry['width']/2)
#print(user_width)

#print("Entering Main Loop...")
window.mainloop()
