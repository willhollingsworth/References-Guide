import tkinter as tk
from tkinter import ttk
from tkinter.constants import COMMAND



''' testing the layout, does not function '''
root = tk.Tk()
root.title('Simple Calculator')

# style = ttk.Style()
# style.theme_use('clam')

e = tk.Entry(root, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, ipadx=50, ipady=30)
l = tk.Entry(root, borderwidth=5)
l.grid(row=0, column=5, rowspan=5, ipadx=30, ipady=200)

def num_click(x):
    print(x)

def sym_click(x):
    print(symbols[x])

symbols = ['÷','x','-','+','=']

#populate numbers
for x in range(3): #rows
    for y in range(3): #columns
        num = 7-(x*3)+y
        button = tk.Button(root,text=num,padx=30,pady=30,\
            command =  lambda cur_num = num : num_click(cur_num))\
            .grid(row=x+1,column=y)

#populate symbols on right            
for x in range(len(symbols)):
    button = tk.Button(root, text = symbols[x],padx=30,pady=30,\
        command =  lambda cur_symb = x : sym_click(cur_symb))\
        .grid(row=x,column=4)
root.mainloop()





