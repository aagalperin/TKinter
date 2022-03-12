from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viwer - by aagalperin")
root.iconbitmap("./imgs/camera32.ico")

# intanciando imagens
my_img1 = ImageTk.PhotoImage(Image.open("./imgs/Goodies - Cool Fire.png"))
my_img2 = ImageTk.PhotoImage(Image.open("./imgs/Goodies - Face Happy.png"))
my_img3 = ImageTk.PhotoImage(Image.open("./imgs/Goodies - Hear Blue.png"))
my_img4 = ImageTk.PhotoImage(Image.open("./imgs/Goodies - Monster Happy.png"))
my_img5 = ImageTk.PhotoImage(Image.open("./imgs/Goodies - Monster.png"))
my_img6 = ImageTk.PhotoImage(Image.open("./imgs/Goodies - Warning Skull.png"))

# criando lista de imagens que será interada
img_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]
MAX_IMG = len(img_list)
MIN_IMG = 0

img_current_position = 0

# Criando espaço onde colocarei minha imagem dentro da janela principal
my_label = Label(image=img_list[img_current_position])
my_label.grid(row=0, column=0, columnspan=3)

# function to go too the next image
def click_forward(img_position):
    global my_label
    global button_forward
    global button_back
    global MAX_IMG

    my_label.grid_forget()
    my_label = Label(image=img_list[img_position])
    my_label.grid(row=0, column=0, columnspan=3)

    if img_position == (MAX_IMG-1):
        button_forward = Button(root, text=" Forward >> ", state=DISABLED)
    else:
        button_forward = Button(root, text=" Forward >> ", command=lambda: click_forward(img_position+1))
    button_forward.grid(row=1, column=2)

    button_back = Button(root, text=" << Back ", command=lambda: click_back(img_position-1))
    button_back.grid(row=1, column=0)

    status = Label(root, text="Image " + str(img_position + 1) + " of " + str(MAX_IMG), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

# function to return to an previous image
def click_back(img_position):
    global my_label
    global button_forward
    global button_back
    global MIN_IMG

    my_label.grid_forget()
    my_label = Label(image=img_list[img_position])
    my_label.grid(row=0, column=0, columnspan=3)

    if img_position == MIN_IMG:
        button_back = Button(root, text=" << Back ", state=DISABLED)
    else:
        button_back = Button(root, text=" << Back ", command=lambda: click_back(img_position - 1))
    button_back.grid(row=1, column=0)

    button_forward = Button(root, text=" Forward >> ", command=lambda: click_forward(img_position+1))
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(img_position +1) + " of " + str(MAX_IMG), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# creating my buttons
button_back = Button(root, text=" << Back ", state=DISABLED)
button_exit = Button(root, text=" Exit ", command=root.quit)
button_forward = Button(root, text=" Forward >> ", command=lambda: click_forward(img_current_position+1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2)


status = Label(root, text="Image " + str(img_current_position + 1) + " of " + str(MAX_IMG), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
