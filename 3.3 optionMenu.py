"""
An option menu is a drop down menu

"""
import tkinter as tk

root = tk.Tk()
root.title("Option Menu")

# this subroutine runs when the button is pressed.
def submit():
	lbl_displayChoice.config(text=choice.get())

# list of options that will be contained in the drop down list
options = ["Java", "python", "C#", "C++", "Ruby"]

# a string variable called choice
# this will be set to the choice that the user makes.
choice = tk.StringVar()
# the initial choice that is displayed
choice.set(options[0])

# the option menu containing the options menu and the variable choice.
# pay attention to the * before the name of the list.
opt_one = tk.OptionMenu(root, choice, *options)

# submit button that causes the label to display the option chosen.
btn_submit = tk.Button(root,
                       command=submit,
                       text="Submit choice")

# the label that displays the user choice.
lbl_displayChoice = tk.Label(root)

opt_one.pack()
btn_submit.pack()
lbl_displayChoice.pack()

root.mainloop()


