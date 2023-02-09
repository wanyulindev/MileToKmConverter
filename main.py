# import tkinter

# or just simply import every single class to make typing faster
# if you're using more than one class.
from tkinter import *

window = Tk()
window.title("AssetsVersionUpdater_Beta")
window.minsize(width=800, height=600)
window.config(padx=200, pady=200)


# Label

first_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# first_label.pack(side="left")
first_label.grid(row=1, column=1)
first_label.config(padx=50, pady=50)


# Either way could override the Keyword Argument's value.

# first_label["text"] = "Changed!"
# first_label.config(text="Changed!")


# Button

def button_clicked():
    # print("Been clicked")
    any_string = input.get()
    first_label.config(text=any_string)


button = Button(text="Click here", command=button_clicked)
button.grid(row=2, column=2)
button.config(padx=20, pady=20)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(row=1, column=3)
new_button.config(padx=30, pady=30)


# Entry

input = Entry(width=10)
input.grid(row=3, column=4)




window.mainloop()


