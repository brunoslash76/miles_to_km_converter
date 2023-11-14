from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# input
input = Entry()
input.grid(column=1, row=0)

# label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# comparison label
comparison_label = Label(text="is equal to")
comparison_label.grid(column=0, row=1)

# result label
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# calc button
def calc_miles_to_km():
  miles = int(input.get())
  km = miles * 1.6
  result_label.config(text=km)


calc_button = Button(text="Calculate")
calc_button.config(command=calc_miles_to_km)

calc_button.grid(column=1, row=2)



window.mainloop()