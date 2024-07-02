import tkinter as tk
from tkinter import Tk, Entry, Button

def insert_number(number):
    current = e1.get()
    e1.delete(0, tk.END)
    e1.insert(0, current + str(number))

def set_operation(operator):
    global first_number
    global operation
    first_number = int(e1.get())
    operation = operator
    e1.delete(0, tk.END)

def clear_entry():
    e1.delete(0, tk.END)

def calculate():
    second_number = int(e1.get())
    e1.delete(0, tk.END)
    if operation == "+":
        e1.insert(0, first_number + second_number)
    elif operation == "-":
        e1.insert(0, first_number - second_number)
    elif operation == "*":
        e1.insert(0, first_number * second_number)
    elif operation == "/":
        if second_number != 0:
            e1.insert(0, first_number / second_number)
        else:
            e1.insert(0, "Error")

if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    root.geometry("250x300")

    e1 = Entry(root, width=20, font=('Arial', 15))
    e1.grid(row=0, column=0, rowspan=1, columnspan=10, padx=10, pady=15)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1)
    ]
    for (text, row, col) in buttons:
        Button(root, text=text, width=6, height=2, command=lambda t=text: insert_number(t)).grid(row=row, column=col,
                                                                                                 padx=5, pady=5)

    Button(root, text="+", width=6, height=2, command=lambda: set_operation('+')).grid(row=1, column=3, padx=2, pady=2)
    Button(root, text="-", width=6, height=2, command=lambda: set_operation('-')).grid(row=2, column=3, padx=2, pady=2)
    Button(root, text="*", width=6, height=2, command=lambda: set_operation('*')).grid(row=3, column=3, padx=2, pady=2)
    Button(root, text="/", width=6, height=2, command=lambda: set_operation('/')).grid(row=4, column=3, padx=2, pady=2)
    Button(root, text="=", width=6, height=2, command=calculate).grid(row=4, column=2, padx=2, pady=2)
    Button(root, text="C", width=6, height=2, command=clear_entry).grid(row=4, column=0, padx=2, pady=2)

    root.mainloop()
