from tkinter import *


def calculate():
    value = entry.get()
    new_value = int(value) * 1.609
    label_value.config(text=new_value)


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(height=50, width=100)
window.config(pady=30, padx=30)

# is equal to label
label = Label(text="is equal to", padx=5, pady=5)
label.grid(row=1, column=0)

# Miles label
label_miles = Label(text="Miles", padx=5, pady=5)
label_miles.grid(row=0, column=2)

# value label
label_value = Label(text="0", padx=5, pady=5)
label_value.grid(row=1, column=1)

# km label
label_km = Label(text="Km", padx=5, pady=5)
label_km.grid(row=1, column=2)

#  Entry
entry = Entry(width=7)
entry.grid(row=0, column=1)

#  Button
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
