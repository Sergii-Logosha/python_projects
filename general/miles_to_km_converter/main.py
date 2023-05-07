# 07.05.23. Sergii Logosha sergiilogosha@gmail.com

# Simple miles to kilometers converter with GUI via Tkinter module

from tkinter import *

MILES_TO_KM_RATIO = 1.60934


def miles_to_km_converting():
    miles = float(input_field.get())
    kilometers = miles * MILES_TO_KM_RATIO
    value_label.config(text=f'{kilometers:.2f}')


window = Tk()
window.title('Miles-Km Converter')
window.minsize()
window.config(padx=10, pady=10)


miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

km_label = Label(text='Kilometers')
km_label.grid(row=1, column=2)

text_label = Label(text='is equal to')
text_label.grid(row=1, column=0)

value_label = Label(text='0')
value_label.grid(row=1, column=1)

button = Button(text='Calculate', command=miles_to_km_converting)
button.grid(row=2, column=1)

input_field = Entry(width=5)
input_field.grid(row=0, column=1)

window.mainloop()
