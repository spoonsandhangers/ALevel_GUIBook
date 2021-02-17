"""
Radio buttons - in a group of radio buttons only one can be selected.
The radio buttons in the same group must have the same variable associated with them
and a command that represents a subroutine or method.
"""
import tkinter as tk

root = tk.Tk()
root.title("Radio Buttons")


def sel():
	selection = choice.get()
	if selection == 1:
		lbl_choice.config(text="You selected Python")
	elif selection == 2:
		lbl_choice.config(text="You selected Java")
	else:
		lbl_choice.config(text="You selected C++")


choice = tk.IntVar()


rbtn_one = tk.Radiobutton(root, text="Python",
                          variable=choice,
                          value=1,
                          command=sel)

rbtn_two = tk.Radiobutton(root, text="Java",
                          variable=choice,
                          value=2,
                          command=sel)

rbtn_three = tk.Radiobutton(root, text="C++",
                            variable=choice,
                            value=3,
                            command=sel)

lbl_choice = tk.Label(root)

rbtn_one.pack()
rbtn_two.pack()
rbtn_three.pack()
lbl_choice.pack()

root.mainloop()

