from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("1255x944")
#photo = PhotoImage(file="20160815_102740.jpg")
image = Image.open("20160815_102740.jpg")
photo = ImageTk.PhotoImage(image)


babuna = Label(image=photo)
babuna.pack()

root.mainloop()
