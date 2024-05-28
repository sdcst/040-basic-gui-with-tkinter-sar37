from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Example")


dogphoto = PhotoImage(file = "dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window, text ="Pochacco!", borderwidth = 3)

label3 = tk.Label(window, text = "a cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", background ="#32F0F6")

label1.grid(row=1, column =3, rowspan = 3)
label2.grid(row=3, column= 4 , columnspan = 2)
label3.grid(row=5,column = 1, columnspan = 5)

window.mainloop()