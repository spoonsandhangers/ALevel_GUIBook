"""
There are 3 layout managers in tkinter pack, grid and place.
In order for a widget to be visible it must be added to a frame or base window using one of the layout managers
You can only use one layout manager per frame/base window.  Although you can use place in combination with pack or grid.
This example uses pack
pack has the options - expand, fill and side.
expand − When set to true, widget expands to fill any space not otherwise used in widget's parent.
fill − Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions:
NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both horizontally and vertically)
side − Determines which side of the parent widget packs against: TOP (default), BOTTOM, LEFT, or RIGHT
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
	btn_one.pack_forget()

lbl_one = tk.Label(root,
                text="This is label one",
                bg = "red",
                font=("Helvetica",10,"bold"))

btn_one = tk.Button(root,
                    command=buttonOne,
                    bg = "blue",
                    text="click this button")

# the labels are added to the base window root using the pack() layout manager.
# label one has the attribute expand set to 1(true) and fill set to Y
# This will expand to fill the space that the parent window has in the Y direction.
# experiment by changing this value to X or BOTH
# the side attribute is set to TOP, experiment with changing this to BOTTOM, LEFT OR RIGHT.
lbl_one.pack(expand=1, fill=tk.Y, side=tk.TOP)  # packs the label onto the parent window
# You can use the same attributes to experiment with this button position.
btn_one.pack(fill=tk.X)  # Packs the button onto the root window.

root.mainloop()

