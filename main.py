from tkinter import *
import playground

window = Tk()

window.title("Converter")
window.minsize(height=100, width=230)
window.config(padx=10, pady=10)


def calculate():
    try:
        inp = input.get()
        print(inp)
        new_inp = float(inp.replace(",", "."))
        print(new_inp)
        mls = round(new_inp/1.6, 2)
        calc_text.config(text=mls)
    except:
        calc_text.config(text="Это не число")


text1 = Label(text="равно")
text1.grid(column=0, row=1)

text2 = Label(text="Миль")
text2.grid(column=2, row=1)

text2 = Label(text="Км")
text2.grid(column=2, row=0)

calc_text = Label(text="0")
calc_text.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

input = Entry()
input.insert(0, "0")
input.grid(column=1, row=0)





window.mainloop()
