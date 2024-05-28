from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Example")


dogphoto = PhotoImage(file = "dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window, text ="Pochacco!", borderwidth = 3)

label3 = tk.Label(window, text = "a cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", background ="#32F0F6")

label1.place(x = 50,y = 5 )
label2.place(x=130, y = 50)
label3.place(x=0, y =100 )

window.mainloop()