"""
There are 3 layout managers in tkinter pack, grid and place.
In order for a widget to be visible it must be added to a frame or base window using one of the layout managers
You can only use one layout manager per frame/base window.  Although you can use place in combination with pack or grid.
This example uses grid.
These are some possible options when using grid:
column − The column to put widget in; default 0 (leftmost column).
row − The row to put widget in; default the first row that is still empty.
padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders
columnspan − How many columns widgetoccupies; default 1
ipadx, ipady − How many pixels to pad widget, horizontally and vertically, inside widget's borders
rowspan − How many rowswidget occupies; default 1
sticky − What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell.
 sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions
 indicating the sides and corners of the cell to which widget sticks
"""
import tkinter as tk

root = tk.Tk()
root.title("Buttons")
root.geometry("500x500")

def buttonOne():
	lbl_one.config(text="Yay! you clicked a button")  # changes the text on lbl_one
	lbl_one.config(bg="yellow")  # changes the background colour of lbl_one to yellow
	# removes the button but does not destroy it.  This can be used with grid as well
	# e.g. .grid_forget()
	btn_one.grid_forget()

lbl_one = tk.Label(root,
                text="This is label one",
                bg = "red",
                font=("Helvetica",10,"bold"))

btn_one = tk.Button(root,
                    command=buttonOne,
                    bg = "blue",
                    text="click this button")

# the labels are added to the parent window root using the grid() layout manager.

# experiment with the different grid attributes.
lbl_one.grid(row=0, column=0, columnspan=3)

btn_one.grid(row=4, column=2)

root.mainloop()

