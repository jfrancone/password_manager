import tkinter

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
        self.website_entry = tkinter.Entry(width = 35)
        self.website_entry.focus()
        self.website_entry.grid(column = 1, row = 1, columnspan=2)
        self.username_entry = tkinter.Entry(width = 35)
        self.username_entry.insert(0,"jfrancone@sandiego.edu")
        self.username_entry.grid(column = 1, row = 2, columnspan=2)
        self.password_entry = tkinter.Entry(width = 17)
        self.password_entry.grid(column = 1, row = 3)
        
        #Buttons
        self.password_generator = tkinter.Button(text = "Generate Password", command = self.generate)
        self.password_generator.grid(column = 2, row = 3)
        self.add_button = tkinter.Button(text = "Add", command = self.add)
        self.add_button.grid(column = 1, row = 4, columnspan = 2)
        
        #Attributes
        self.website = None
        self.username = None
        self.password = None

    #Functions
    def run(self):
        #print("Entering Main Loop...")
        self.window.mainloop()

    def generate(self):
        print("Generating Password")

    def add(self):
        self.website = self.website_entry.get()
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        print(f"Website = {self.website}, Username = {self.username}, Password = {self.password}")
        with open("data.txt", mode = "a") as file:
            file.write(f"{self.website} | {self.username} | {self.password}\n")
        self.website_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

