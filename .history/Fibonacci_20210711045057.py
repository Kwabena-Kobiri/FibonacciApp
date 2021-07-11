from tkinter import *

root = Tk()
root.title('Fibonacci Number Finder')
root.geometry('600x400')

def button_command():
    print("test")
    return None

entry1 = Entry(root, width=20)
entry1.pack()

button = Button(root, text='Button', command=button_command, font=('bold', 12), pady=20)
button.pack()


root.mainloop()