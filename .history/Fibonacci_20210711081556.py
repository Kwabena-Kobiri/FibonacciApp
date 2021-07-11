from tkinter import *

root = Tk()
root.title('Fibonacci Number Finder')
root.geometry('500x300')

def button_command():
    print("test")
    return None

# Label for description of application
header_label = Label(root, text='This is a Simple Program to find the values of a \ngiven index in a Fibonacci sequence from 1 to 24',
                        font=('bold', 14))
header_label.grid(row=0, columnspan=3, pady=10, padx=30, sticky=EW)

# Label for entry of starting digit
entry1_label = Label(root, text='Enter starting number', font=(12))
entry1_label.grid(row=2, column=0, pady=25, padx=20)

# Starting digit entry cell
entry1 = Entry(root, width=20)
entry1.grid(row=2, column=1, sticky=W, padx=10, pady=25)

# Label for entry of total number of elements to be generated
entry1_label = Label(root, text='Enter number of elements to generate', font=(12))
entry1_label.grid(row=3, column=0, pady=25, padx=20)

# Total number of elements to be generated entry cell
entry1 = Entry(root, width=20)
entry1.grid(row=3, column=1, sticky=W, padx=10, pady=25)

# Button for generating Fibonacci sequence
button = Button(root, text='Generate Sequence', command=button_command, font=('bold', 12))
button.grid(row=4)

root.mainloop()