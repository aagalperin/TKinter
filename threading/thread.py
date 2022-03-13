from tkinter import *
import time
from random import randint
import threading

def five_seconds():
    time.sleep(5)
    my_label.config(text="5 Seconds is up")


def rand_number():
    nb = randint(1, 100)
    random_label.config(text="Random Number : " + str(nb))


root = Tk()
root.title("Learning  threads - by aagalperin")
root.geometry("300x300")

my_label = Label(root, text="Hello There!")
my_label.pack(pady=5)

my_button1 = Button(root, text="5 Seconds", command=threading.Thread(target=five_seconds).start())
my_button1.pack(pady=5)

my_button2 = Button(root, text="Pick random Number", command=rand_number)
my_button2.pack(pady=5)

random_label = Label(root, text="")
random_label.pack(pady=5)

root.mainloop()
