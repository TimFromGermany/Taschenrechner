'''
Main.py
'''

from tkinter import *

def addition(z1, z2):
    return z1+z2

def subtraktion(z1, z2):
    return z1-z2

def multiplikation(z1, z2):
    return z1*z2

def division(z1, z2):
    if z2 != 0:
        return z1/z2
    else:
        return None

def test():
    print("Test")




top = Frame()
top.pack()
widget = Button(top, text = '+', command = test).pack(side=LEFT)
widget = Button(top, text = '-', command = test).pack(side=RIGHT)
top.mainloop()

# erg = addition(1, 9)
# print(erg)
