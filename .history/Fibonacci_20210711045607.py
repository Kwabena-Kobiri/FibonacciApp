from tkinter import *

root = Tk()
root.title('Fibonacci Number Finder')
root.geometry('600x400')

def button_command():
    print("test")
    return None

header_label = Label(root, text='This is a Simple Program to find the values of a given number in a Fibonacci sequence',
                        font=('italic', 14), pady=20, padx=20)
header_label.pack()

entry1 = Entry(root, width=20)
entry1.pack()

button = Button(root, text='Button', command=button_command, font=('bold', 12), pady=20)
button.pack()


root.mainloop()