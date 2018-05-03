from tkinter import Tk, Label, Button

class InfoWindow:
    def __init__(self, master, Text):
        self.master = master
        master.title("You have new Emails")

        self.label = Label(master, text=Text)
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
