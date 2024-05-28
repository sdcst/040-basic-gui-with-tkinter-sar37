from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("400x40")

entry1 = tk.Entry(window, text="", borderwidth = 3)
label1 = tk.Label(window, text = "x")
label2 = tk.Label(window, text = "=", borderwidth = 3)
entry2 = tk.Entry(window, text="", borderwidth = 5)

entry1.place(x=0, y =0)
label1.place(x=50, y = 0)
label2.place(x = 100, y = 0)
entry2.place(x = 150, y = 0)
window.mainloop()

