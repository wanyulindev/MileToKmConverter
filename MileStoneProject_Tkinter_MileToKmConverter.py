from tkinter import *

default_miles = 0

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=250)
window.config(padx=30, pady=50)


def input_assigned():

    any_string = miles_input.get()
    to_km = round(int(any_string) * 1.60934)
    km_result.config(text=f"{to_km}")


button = Button(text="Calculate", command=input_assigned)
button.place(x=115, y=100)
button.config(padx=10, pady=10)


miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.place(x=200, y=0)
miles_label.config(padx=30, pady=10)

km_label = Label(text="Km", font=("Arial", 20))
km_label.place(x=200, y=50)
km_label.config(padx=30, pady=10)

text_label = Label(text="is equal to", font=("Arial", 18))
text_label.place(x=-10, y=50)
text_label.config(padx=30, pady=10)

km_result = Label(text=default_miles, font=("Arial", 20))
km_result.place(x=135, y=50)
km_result.config(padx=30, pady=10)

miles_input = Entry(width=8)
miles_input.place(x=125, y=13)


window.mainloop()


