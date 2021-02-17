"""
This uses a sub library of tkinter ttk
The Notebook object of ttk provides tabs

"""
import tkinter as tk
from tkinter import ttk  # imports the ttk library

root = tk.Tk()
root.title("Tabbed widget")
tabControl = ttk.Notebook(root)  # creates a notebook with tabs

tab1 = ttk.Frame(tabControl)  # creates a tab called tab1
tab2 = ttk.Frame(tabControl)  # creates a tab called tab2

# adds each tab to the notebook and specifies the text on each one.
tabControl.add(tab1, text="Tab 1")
tabControl.add(tab2, text="Tab 2")
tabControl.pack()

a_frame = tk.Frame(tab1,
                   width=300,
                   height=200,
                   bg="green",
                   bd=8,
                   relief="sunken",
                   padx=30,
                   pady=30)

b_frame = tk.Frame(tab2,
                   width=300,
                   height=200,
                   bg="yellow",
                   bd=8,
                   relief="sunken",
                   padx=30,
                   pady=30)

lbl_two = tk.Label(b_frame,
                   text="This is on tab 2",
                   padx=10,
                   pady=10)

lbl_one = tk.Label(a_frame,
                   text="This is on tab 1",
                   padx=10,
                   pady=10)

lbl_one.grid(row=0, column=0)
lbl_two.grid(row=0, column=0)


a_frame.grid(row=0, column=0)
b_frame.grid(row=0, column=0)

root.mainloop()
