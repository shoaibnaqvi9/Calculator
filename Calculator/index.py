from tkinter import *

def insert_number(number):
    current_text=e1.get()
    e1.delete(0,END)
    e1.insert(0,current_text+str(number))

def set_operation(operation):
    global first_number, math_operation
    first_number = int(e1.get())
    math_operation = operation
    e1.delete(0, END)

def calculate():
    second_number = int(e1.get())
    e1.delete(0, END)
    if math_operation == '+':
        result = first_number + second_number
    e1.insert(0, str(result))

def clear():
    e1.delete(0,END)

if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    l1 = Label(root,text='Calculator')
    l1.grid(row=0, column=0)
    e1 = Entry(root)
    e1.grid(row=0, column=1)
    b1 = Button(root,text="1",width=9,height=3,command=lambda :insert_number(1))
    b1.grid(row=1, column=0,columnspan=1)
    b2 = Button(root, text="2",width=9,height=3, command=lambda: insert_number(2))
    b2.grid(row=1, column=1, columnspan=1)
    b3 = Button(root, text="3",width=9,height=3, command=lambda: insert_number(3))
    b3.grid(row=1, column=2, columnspan=1)
    b4 = Button(root, text="4",width=9,height=3, command=lambda: insert_number(4))
    b4.grid(row=2, column=0, columnspan=1)
    b5 = Button(root, text="5",width=9,height=3, command=lambda: insert_number(5))
    b5.grid(row=2, column=1, columnspan=1)
    b6 = Button(root, text="6",width=9,height=3, command=lambda: insert_number(6))
    b6.grid(row=2, column=2, columnspan=1)
    b7 = Button(root, text="7",width=9,height=3, command=lambda: insert_number(7))
    b7.grid(row=3, column=0, columnspan=1)
    b8 = Button(root, text="8", width=9, height=3, command=lambda: insert_number(8))
    b8.grid(row=3, column=0, columnspan=1)
    b9 = Button(root, text="9", width=9, height=3, command=lambda: insert_number(9))
    b9.grid(row=3, column=0, columnspan=1)

    # For Addition:
    b_add = Button(root, text="+", width=9, height=3, command=lambda: set_operation('+'))
    b_add.grid(row=4, column=0, columnspan=1)

    b_equals = Button(root, text="=", width=9, height=3, command=calculate)
    b_equals.grid(row=4, column=2, columnspan=1)

    b_clear = Button(root, text="AC", width=9, height=3, command=lambda :clear())
    b_clear.grid(row=1, column=3, columnspan=1)


    root.mainloop()
