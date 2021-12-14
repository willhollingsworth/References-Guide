
'''
Tkinter Course - Create Graphic User Interfaces in Python Tutorial
https://www.youtube.com/watch?v=YXPyB4XeYLA
'''


import tkinter as tk
root = tk.Tk()
def my_click():
    my_label = tk.Label(root,text='You clicked!')
    my_label.pack()

# Create a label widget
my_label = tk.Label(root,text='Hello World!')
my_button = tk.Button(root,text='click me',command=my_click)

# Shove it onto the screen
my_label.pack()
my_button.pack()
root.mainloop()