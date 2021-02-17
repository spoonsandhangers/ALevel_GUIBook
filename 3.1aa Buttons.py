"""
Example of buttons without using a class
these widgets are added to the root (base window) using pack() instead of grid.
the button has a command buttonOne.  This means when the button is clicked the subroutine buttonOne() executes
this subkroutine uses .config to change the text and background colour of lbl_one.
It also uses pack_forget() to remove the button from root.
"""
import tkinter as tk

root = tk.Tk()
root.title("Buttons")

def buttonOne():
	lbl_one.config(text="Yay! you clicked a button")  # changes the text on lbl_one
	lbl_one.config(bg="yellow")  # changes the background colour of lbl_one to yellow
	# removes the button but does not destroy it.  This can be used with grid as well
	# e.g. .grid_forget()
	btn_one.pack_forget()

lbl_one = tk.Label(root,
                text="This is label one",
                bg = "red",
                font=("Helvetica",10,"bold"))

btn_one = tk.Button(root,
                    command=buttonOne,
                    text="click this button")

# the labels are added to the base window root using the pack() layout manager.
lbl_one.pack()  # packs the label onto the root window
btn_one.pack()  # Packs the button onto the root window.

root.mainloop()

