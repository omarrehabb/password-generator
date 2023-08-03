import tkinter as tk
from tkinter import *
import random

root = tk.Tk()

#Main function to generate password
def generatePass():
    
    #loop to clear space for each new list of passwords / refresh output
    for widget in pass_frame.winfo_children():
        widget.destroy()

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = '0123456789'
    symbols = "@#$%&^*()_<>/-"
    
    upper, lower, nums, syms = False, False, False, False
    if up.get() == 1:
        upper = True         
    if low.get() == 1:
        lower = True
    if num.get() == 1:
        nums = True
    if sym.get() == 1:
        syms = True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

    length = int(lengthEntry.get())
    amount = int(amountEntry.get())

    #error handling
    if len(all) < length:
        error = "Please select more boxes or \ndecrease number of\n characters to " + str(len(all)) 
        #print(error)
        error_label = tk.Label(pass_frame, text=error, bg="#263D42", font=("Helvetica", 11), width= 180)
        error_label.pack()
    x = 1
    for x in range(amount):
        password = "".join(random.sample(all, length))
        x += 1
        out = str(x) + " - " + password
        #print(str(x) + " - " + password)
        #pass_label = tk.Label(pass_frame, text=out,bg="#263D42", width=150)
        w = Text(pass_frame,height=1, borderwidth=0)
        w.insert(1.0, out)
        w.pack()
        w.configure(state="disabled")
        #pass_label.pack()
    

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

#Title of app
title = tk.Label(canvas, text="Password generator", font=("Helvetica", 24), bg="#263D42",fg="white" )
title.place(x=220, y= 20)

#Frame of whole app
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Frame for password / 2 frames so password frame can be refreshed each time button is pressed
pass_frame = tk.Frame(frame, bg="white")
pass_frame.place(relwidth=0.4, relheight=0.99, relx=0.3, rely=0.01)

#Default length is 20 for number of characters
defaultLength = tk.StringVar(root, value= "20")
lengthEntry = tk.Entry(frame,bg="#263D42", width=5, textvariable=defaultLength)
lengthEntry.place(x=140,y=206)

length = tk.Label(frame, text="Number of characters", bg="#263D42", width= 17)
length.place(x=10,y=205)

#Default amount of passwords generated is 10
defaultAmount = tk.StringVar(root, value="10")
amountEntry = tk.Entry(frame,bg="#263D42", width=5, textvariable=defaultAmount)
amountEntry.place(x=140,y=230)

amount = tk.Label(frame, bg="#263D42",text="Amount of passwords", width=17)
amount.place(x=10, y= 229)

#Button to generate passwords, links to generatePass function
generate = tk.Button(root, text="Generate passwords", padx=10, pady=5, fg= "white", bg="#263D42", command=generatePass)
generate.pack()

#Checkboxes for choosing passowrd requirments
up = tk.IntVar()
low = tk.IntVar()
num = tk.IntVar()
sym = tk.IntVar()
upperCase = tk.Checkbutton(frame,text = "Upper case",activebackground="black" , activeforeground="blue" 
                 ,bg="#263D42",bd=10, 
                 onvalue = 1, offvalue = 0,variable=up)
upperCase.place(x=10, y=25)

lowerCase = tk.Checkbutton(frame,text = "Lower case",activebackground="black" , activeforeground="blue" 
                 ,bg="#263D42",bd=10, 
                 onvalue = 1, offvalue = 0, variable=low)
lowerCase.place(x=10, y=70)

numbers = tk.Checkbutton(frame, text = "Numbers",activebackground="black" , activeforeground="blue" 
                 ,bg="#263D42",bd=10, 
                 onvalue = 1, offvalue = 0,variable=num)
numbers.place(x=10, y=115)

symbols = tk.Checkbutton(frame, text = "Symbols",activebackground="black" , activeforeground="blue" 
                 ,bg="#263D42",bd=10, 
                 onvalue = 1, offvalue = 0, variable=sym)
symbols.place(x=10, y=160)

root.mainloop()
