
from tkinter import *

# Funktion, die aufgerufen wird, wenn eine Zahl oder ein Operator gedrückt wird
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

# Funktion, die aufgerufen wird, wenn der Gleichheits-Button gedrückt wird
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Calculation error")
        equation_text = ""

# Funktion, die aufgerufen wird, wenn der Clear-Button gedrückt wird
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

# Hauptfenster
window = Tk()
window.title("Calculator")
window.geometry("500x500")

# Variable für die Gleichung
equation_text = ""
equation_label = StringVar()

# Anzeige-Label für die Gleichung
label = Label(window, textvariable= equation_label, font=("consolas", 24), bg="black", fg="white", width=26, height=2)
label.pack()

# Frame für die Buttons
frame = Frame(window)
frame.pack()


# Parameter für die Buttons
button_params = {'height': 2, 'width': 5, 'font': ("consolas", 20)}

# Nummern- und Operator-Buttons im Grid
button1 = Button(frame, text="1", command=lambda: button_press(1), **button_params)
button1.grid(row=0, column=0)

button2 = Button(frame, text="2", command=lambda: button_press(2), **button_params)
button2.grid(row=0, column=1)

button3 = Button(frame, text="3", command=lambda: button_press(3), **button_params)
button3.grid(row=0, column=2)

button4 = Button(frame, text="4", command=lambda: button_press(4), **button_params)
button4.grid(row=1, column=0)

button5 = Button(frame, text="5", command=lambda: button_press(5), **button_params)
button5.grid(row=1, column=1)

button6 = Button(frame, text="6", command=lambda: button_press(6), **button_params)
button6.grid(row=1, column=2)

button7 = Button(frame, text="7", command=lambda: button_press(7), **button_params)
button7.grid(row=2, column=0)

button8 = Button(frame, text="8", command=lambda: button_press(8), **button_params)
button8.grid(row=2, column=1)

button9 = Button(frame, text="9", command=lambda: button_press(9), **button_params)
button9.grid(row=2, column=2)

button0 = Button(frame, text="0", command=lambda: button_press(0), **button_params)
button0.grid(row=3, column=0)

plus = Button(frame, text="+", command=lambda: button_press("+"), **button_params)
plus.grid(row=0, column=3)

minus = Button(frame, text="-", command=lambda: button_press("-"), **button_params)
minus.grid(row=1, column=3)

times = Button(frame, text="x", command=lambda: button_press("*"), **button_params)  # Verwende "*" für Multiplikation
times.grid(row=2, column=3)

divide = Button(frame, text="/", command=lambda: button_press("/"), **button_params)
divide.grid(row=3, column=3)

equals_button = Button(frame, text="=", command=lambda: equals(), **button_params)
equals_button.grid(row=3, column=2)

decimal = Button(frame, text=".", command=lambda: equals(), **button_params)
decimal.grid(row=3, column=1)

clear_button = Button(frame, text="C", command=lambda: clear(), **button_params)
clear_button.grid(row=5, column=3)

window.mainloop()

