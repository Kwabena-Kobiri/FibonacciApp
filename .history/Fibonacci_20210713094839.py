from tkinter import *

root = Tk()
root.title('Fibonacci Number Finder')
root.geometry('500x550')

def clear_fields():
    # value1 = entry1.get()
    # value2 = entry2.get()
    # values = [value1, value2]
    entry1.delete(0, END)
    entry2.delete(0, END)
    # sequence_items(values)

def generate_fibonacci():
    value1 = int(entry1.get())
    value2 = int(entry2.get())
    # sequence = [value1, value2]
    print(value1, value2)
    num1 = 1
    num2 = 1
    sum = 0
    sequence = [num1, num2]

    for i in range(2, value1):
            sum = num1 + num2
            num1 = num2
            num2 = sum
            sequence.append(sum)
    sequence_items(sequence)

    # Check if starting number is equal to 1
    # if value2.strip() != 1:
    #     print('Starting number should be the integer one (1)')
    # elif 0 > value1  or value1 > 24:
    #     print('Number of elements to be generated should be between the integers zero(0) and twenty four(24)')
    # else:
    #     for i in range(2, value1):
    #         sum = num1 + num2
    #         num1 = num2
    #         num2 = sum
    #         sequence.append(sum)
    #     sequence_items(sequence)

def sequence_items(items):
    # Inserting items into the ListBox
    for i in range(len(items)):
        sequence_list.insert(i, items[i])

    # Colorize alternating lines of the listbox - #f0f0ff
    for i in range(0,len(items),2):
        sequence_list.itemconfigure(i, background='blue', fg='white')    


# Label for description of application
header_label = Label(root, text='This is a Simple Program to find the values of a \ngiven index in a Fibonacci sequence from 1 to 24',
                        font=('bold', 14), bg='aqua')
header_label.grid(row=0, columnspan=3, pady=10, padx=30, sticky=EW)

# Label for entry of total number of elements to be generated
entry1_label = Label(root, text='Enter number of elements to generate', font=(12), bg='#8e2de2', fg='white')
entry1_label.grid(row=2, column=0, pady=25, padx=20, sticky=E)

# Total number of elements entry cell
entry1 = Entry(root, width=20)
entry1.grid(row=2, column=1, sticky=W, padx=10, pady=25)

# Label for entry of Starting digit
entry2_label = Label(root, text='Enter starting number', font=(12), bg='#8e2de2', fg='white')
entry2_label.grid(row=3, column=0, padx=20, sticky=E)

# Starting digits entry cell
entry2 = Entry(root, width=20)
entry2.grid(row=3, column=1, sticky=W, padx=10)

# Button for generating Fibonacci sequence
button1 = Button(root, text='Generate Sequence', command=generate_fibonacci, font=('bold', 10), fg='white', bg='#1e9688')
button1.grid(row=6,column=1, pady=50, sticky=W)

# Label for generated Fibonacci sequence
generated_label = Label(root, text='Generated Fibonacci Sequence', font=('bold',12), bg='#f80759', fg='white')
generated_label.grid(row=8, column=0, sticky=W, padx=5)

# ListBox to display the generated sequence
sequence_list = Listbox(root, width=50, height=5, font=('bold', 10))
sequence_list.grid(row=9, columnspan=3, pady=20, padx=10, sticky=EW)

# Button for clearing the list of generated sequences.
button2 = Button(root, text='Clear field', font=('bold',10), command=clear_fields, fg='white', bg='#1e9688')
button2.grid(row=10, column=1, pady=10, padx=10, sticky=W)

# Label for styling
style_label = Label(root, bg='aqua')
style_label.grid(row=14, column=0, columnspan=4, sticky=EW, padx=20, rowspan=3)

root.mainloop()