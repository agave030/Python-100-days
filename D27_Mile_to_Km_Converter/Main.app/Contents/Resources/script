from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=2, row=1)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=1, row=2)

miles = Label(text='Miles')
miles.grid(column=3, row=1)

km_voca = Label(text="Km")
km_voca.grid(column=2, row=2)

km_label = Label(text='0')
km_label.grid(column=2, row=2)


button = Button(text='Calculate', command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()
