import tkinter
from tkinter import messagebox
from password_generator import generate
import pyperclip
import json

class Engine():
    def __init__(self):
        #create window
        self.window = tkinter.Tk()
        self.window.title("Password Manager")
        self.window.config(padx=20, pady=20)
        self.canvas = tkinter.Canvas(width=200, height=200)
        #create logo
        self.logo_img = tkinter.PhotoImage(file = "logo.png")
        self.logo_width = self.logo_img.width()
        self.logo_height = self.logo_img.height()
        print(f"width = {self.logo_width}, height = {self.logo_height}")
        self.canvas.create_image(self.logo_width/2, self.logo_height/2, image=self.logo_img)
        self.canvas.grid(column = 1, row = 0)

        #Labels
        self.website_label = tkinter.Label(text = "Website:")
        self.website_label.grid(column = 0, row = 1)
        self.username_label = tkinter.Label(text = "Email/Username:")
        self.username_label.grid(column = 0, row = 2)
        self.password_label = tkinter.Label(text = "Password:")
        self.password_label.grid(column = 0, row = 3)
        
        #Entries
        self.website_entry = tkinter.Entry(width =35)
        self.website_entry.focus()
        self.website_entry.grid(column = 1, row = 1)
        self.username_entry = tkinter.Entry(width = 35)
        self.username_entry.insert(0,"jfrancone@sandiego.edu")
        self.username_entry.grid(column = 1, row = 2)
        self.password_entry = tkinter.Entry(width = 35)
        self.password_entry.grid(column = 1, row = 3)
        
        #Buttons
        self.search_button = tkinter.Button(text = "Search", command = self.search)
        self.search_button.grid(column = 2, row = 1)
        self.password_generator = tkinter.Button(text = "Generate Password", command = self.generate_password)
        self.password_generator.grid(column = 2, row = 3)
        self.add_button = tkinter.Button(text = "Add", command = self.add)
        self.add_button.grid(column = 1, row = 4)
        
        #Attributes
        self.website = None
        self.username = None
        self.password = None

    #Functions
    def run(self):
        #print("Entering Main Loop...")
        self.window.mainloop()

    def add(self):
        print("Add Button Has Been Clicked")
        self.website = self.website_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        new_data = {
            self.website:{
                "email": self.username,
                "password": self.password,

        }}
        print(f"Website = {self.website}, Username = {self.username}, Password = {self.password}")
        if (len(self.website) == 0) or (len(self.username) == 0) or (len(self.password) == 0):
            messagebox.showerror(title = "Input Error", message = "Do not leave any fields empty")
        else:    
            try:
                with open("data.json", mode = "r") as file:
                    #dumps this info (new_data dictionary) into the json file
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode = 'w') as file:
                    json.dump(new_data, file, indent = 4)
            else:
                with open("data.json", mode = 'w') as file:
                    json.dump(data, file, indent = 4)

            self.website_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

    def generate_password(self):
        self.password_entry.delete(0, 'end')
        password = generate()
        self.password = password
        self.password_entry.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo(title=None, message = "Your Password has been copied to your clipboard!")

    def search(self):
        empty_dict = {}
        self.website = self.website_entry.get()
        try:
            with open("data.json", mode = 'r') as file:
                data = json.load(file)
                print(data)
        except FileNotFoundError:
            messagebox.showerror(title = "Error", message = "No Data File Found. \n File is being Added.")
            with open("data.json", mode = 'w') as file:
                json.dump(empty_dict, file, indent = 4)
        except json.decoder.JSONDecodeError:
            messagebox.showerror(title = "Error", message = "No details for the website exist")
        else:
            try:
                pw_info = data[self.website]
                print(pw_info)
                email = pw_info['email']
                password = pw_info['password']
                messagebox.showinfo(title = "Password Info", message = f"Website = {self.website} \n Email/Username = {email} \n Password = {password}")

            except KeyError:
                messagebox.showerror(title = "Error", message = "No details for the website exist")
