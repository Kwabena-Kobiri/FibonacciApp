from tkinter import *

root = Tk()
root.geometry('600x400')

def button_command():
    print("test")
    return None

entry1 = Entry(root, width=20)
entry1.pack()

Button(root, text='Button', command=button_command).pack()


root.mainloop()