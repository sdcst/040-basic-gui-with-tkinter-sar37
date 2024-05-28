from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("T-Town Veterinary Clinic database ")
window.geometry("650x250")

button1 = tk.Button(window, text ="Search by Name")

entry1 = tk.Entry(window, text = "", borderwidth=3)

dogphoto = PhotoImage(file = "dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window, text = "Client Database", borderwidth=3 )

label3 = tk.Label ( window, text ="Name", borderwidth=3 )
entry2 = tk.Entry (window, text = "", borderwidth = 3 )

label4 = tk.Label ( window, text = "Type", borderwidth=3)
entry3 = tk.Entry (window, text = "", borderwidth = 3 )

label5 = tk.Label (window, text ="Breed", borderwidth=3)
entry4 = tk.Entry (window, text = "", borderwidth = 3 )

label6 = tk.Label (window, text = "Owner", borderwidth=3)
entry5 = tk.Entry(window ,text = "", borderwidth = 3 )

label7 = tk.Label (window, text ="Birthdate", borderwidth=3)
entry6 = tk.Entry(window ,text = "", borderwidth = 3 )

button2 = tk.Button (window, text = "<Previous", borderwidth=3)

button3 = tk.Button (window, text = "save Entry", borderwidth = 3)

button4 = tk.Button (window, text ="Next<", borderwidth = 3)

button1.grid (row=1, column=4)
entry1.grid(row=1,column = 5)
label1.grid(row=1 , column = 1, rowspan = 3)
label2.grid(row=2,column = 3)
label3.grid(row=4,column=1)
entry2.grid(row=5,column = 1)
label4.grid (row=4,column = 2)
entry3.grid (row= 5,column=2)
label5.grid(row=4,column = 3)
entry4.grid (row=5, column=3)
label6.grid(row=4, column=4)
entry5.grid(row=5, column=4)
label7.grid (row=4,column=5)
entry6.grid(row= 5,column=5)
button2.grid(row=6,column=1)
button3.grid(row=6,column=3)
button4.grid(row=6, column =5 )

window.mainloop()
