from tkinter import *

root = Tk()
root.title('Fibonacci Number Finder')
root.geometry('600x400')

def button_command():
    print("test")
    return None

header_label = Label(root, text='This is a Simple Program to find the values of a \ngiven number in a Fibonacci sequence',
                        font=('bold', 14), pady=20, padx=40)
header_label.grid(row=0)

entry1 = Entry(root, width=20)
entry1.grid(row=2, pady=20)

button = Button(root, text='Button', command=button_command, font=('bold', 12), pady=20, padx=20)
button.grid(row=4)

root.mainloop()