"""
Check boxes have 2 states on or off - 1 or 0
they can be labelled with text or an image
You need an intVar() to hold the checkbox state.
when the button is pressed the sate of the var1 and var2 is
tested to see what choices have been made.
These are displayed on the lbl_one.
"""
import tkinter as tk

root = tk.Tk()
root.title("checkboxes")

var1 = tk.IntVar()
var2 = tk.IntVar()


def showChoices():
	if(var1.get()==1) and (var2.get()==1):
		lbl_show.config(text="you like Python and Java!")
	elif (var1.get()==1) and (var2.get()==0):
		lbl_show.config(text="you only like Python")
	elif (var1.get()==0) and (var2.get()==1):
		lbl_show.config(text="you only like Java")
	else:
		lbl_show.config(text="you don't like either!")

	lbl_show.grid(row=2, column=1)


ckb_one = tk.Checkbutton(root,
                         text="Python",
                         variable=var1)

ckb_two = tk.Checkbutton(root,
                         text="Java",
                         variable=var2)

btn_show = tk.Button(root,
                     text="Show choices",
                     command=showChoices)

lbl_show = tk.Label(root)

ckb_one.grid(row=0, column=0)
ckb_two.grid(row=1, column=0)
btn_show.grid(row=2, column=0)


root.mainloop()
