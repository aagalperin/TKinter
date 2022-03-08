from tkinter import *

root = Tk()
root.title("Calculator")

# adding an icon
root.iconbitmap('icon.ico')

# creatig myy imput entry
data_entry = Entry(root, width=35, borderwidth=5)
data_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=2)

# creates the number that we want to add as an imput
def button_click(number):
    current_data = data_entry.get()
    data_entry.delete(0, END)
    data_entry.insert(0, str(current_data) + str(number))


#Deletes everything that is in the imput widget
def button_clear():
    data_entry.delete(0, END)


def button_add():
    first_number = data_entry.get()
    global partial_result
    global math
    math = "addition"
    partial_result = float(first_number)
    data_entry.delete(0, END)


def button_subtract():
    first_number = data_entry.get()
    global partial_result
    global math
    math = "subtract"
    partial_result = float(first_number)
    data_entry.delete(0, END)


def button_multiply():
    first_number = data_entry.get()
    global partial_result
    global math
    math = "multiply"
    partial_result = float(first_number)
    data_entry.delete(0, END)


def button_divide():
    first_number = data_entry.get()
    global partial_result
    global math
    math = "divide"
    partial_result = float(first_number)
    data_entry.delete(0, END)


def button_equal():
    second_number = data_entry.get()
    data_entry.delete(0, END)
    if math == "addition":
        data_entry.insert(0, partial_result + float(second_number))
    if math == "subtract":
        data_entry.insert(0, partial_result - float(second_number))
    if math == "multiply":
        data_entry.insert(0, partial_result * float(second_number))
    if math == "divide":
        data_entry.insert(0, partial_result / float(second_number))


# Creating number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Creating math symbols
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

# creating behavieur
button_equal = Button(root, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=125, pady=20, command=button_clear)

# Adding buttons in the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2)

button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()
