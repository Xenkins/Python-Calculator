import tkinter as tk
from tkinter import *

#sets up window
m = tk.Tk(className = "Calculator")

m.geometry('160x240')


string = ""
answer = ""
equation = tk.StringVar()

#functions
def click(num):
    global string
    string += str(num)
    equation.set(string)

def solve():
    global string
    global answer
    try:
        answer = str(eval(string))
        equation.set(answer)
        string = ""
    except:
        string = ""
        equation.set("Error")


def multiply():
    global string
    string += "*"
    equation.set(string)

def addition():
    global string
    string += "+"
    equation.set(string)

def subtract():
    global string
    string += "-"
    equation.set(string)

def division():
    global string
    string += "/"
    equation.set(string)

def clear():
    global string
    string = ""
    equation.set(string)

def change_sign():
    global string
    string = int(string)
    string = str(-1*string)
    equation.set(string)


#buttons:

b1 = tk.Button(m, text = "1", command = lambda: click(1))
b1.place(x= 0, y= 40, height = 40, width = 40)


b2 = tk.Button(m, text = "2", command = lambda: click(2))
b2.place(x= 40, y= 40, height = 40, width = 40)

b3 = tk.Button(m, text = "3", command = lambda: click(3))
b3.place(x= 80, y= 40, height = 40, width = 40)

b4 = tk.Button(m, text = "4", command = lambda: click(4))
b4.place(x= 0, y= 80, height = 40, width = 40)

b5 = tk.Button(m, text = "5", command = lambda: click(5))
b5.place(x= 40, y=80, height = 40, width = 40)

b6 = tk.Button(m, text = "6", command = lambda: click(6))
b6.place(x= 80, y= 80, height = 40, width = 40)

b7 = tk.Button(m, text = "7", command = lambda: click(7))
b7.place(x= 0, y= 120, height = 40, width = 40)

b8 = tk.Button(m, text = "8", command = lambda: click(8))
b8.place(x= 40, y= 120, height = 40, width = 40)

b9 = tk.Button(m, text = "9", command = lambda: click(9))
b9.place(x= 80, y= 120, height = 40, width = 40)

b0 = tk.Button(m, text = "0", command = lambda: click(0))
b0.place(x= 0, y= 160, height = 40, width = 40)

clear = tk.Button(m, text = "Clear", command = clear)
clear.place(x = 40, y = 160, height = 40, width = 40)

add = tk.Button(m, text = "+", command = addition)
add.place(x = 120, y = 40, height = 40, width = 40)

sub = tk.Button(m, text = "-", command = subtract)
sub.place(x = 120, y = 80, height = 40, width = 40)

multi = tk.Button(m, text = "x", command = multiply)
multi.place(x = 120, y= 120, height = 40, width = 40)

divide = tk.Button(m, text = "/", command = division)
divide.place(x = 120, y = 160, height = 40, width = 40)

neg = tk.Button(m, text = "+/-", command = change_sign)
neg.place(x = 80, y = 160, height = 40, width = 40)

equals = tk.Button(m, text = "=", command = solve)
equals.place(x= 0, y = 200, height = 40, width = 160)








#display
dis= Entry(m, textvariable=equation)
dis.configure(background = "white")
dis.place(x = 0, y= 0, height = 40, width = 160)


#runs program
m.mainloop()