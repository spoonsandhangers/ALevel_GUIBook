# """
# labels can contain images as well as text.
# images must first be assigned to a variable in tkinter before they can be used.
# To do this a photoimage is created.
# We can store all the images in the same folder as our python files, but this some becomes
# crowded if we are building a large application.
# As each operating system has a different way of referencing the path to a file e.g.
# windows: c:\users\sarah\documents\pythonfiles
# mac /users/sarah/documents/pythonfiles
# it is good practice to first find the path to the python folder you are using and then
# to set the path to a separate folder containing the images.  Then no matter what operating system is
# being used the path is still valid and you can store your images in a folder.
# This code combines a label a button and a drop down list.
# Both text and an image are added to the label.
# """
from tkinter import *
import os
from pathlib import Path

window = Tk()

# Get the path to this file.
# this is so that the file can be referenced whether it is on a windows/mac or linux OS
this_folder = Path.cwd()
print(this_folder)
img_folder = os.path.join(this_folder, "img")  # join adds the string onto the path

# create the photo images to add to the labels
pythonpath = os.path.join(img_folder, "pythonIcon.PNG")  # use join again to add the image file to the path
pythonpic = PhotoImage(file=pythonpath)  # create a tkinter PhotoImage to use in the application.

javapath = os.path.join(img_folder, "javaicon.PNG")
javapic = PhotoImage(file=javapath)

cpluspath = os.path.join(img_folder, "C++Icon.PNG")
cpluspic = PhotoImage(file=cpluspath)

javascriptpath = os.path.join(img_folder, "javascripticon.PNG")
javascriptpic = PhotoImage(file=javascriptpath)

phppath = os.path.join(img_folder, "phpicon.PNG")
phppic = PhotoImage(file=phppath)

csharppath = os.path.join(img_folder, "csharpicon.PNG")
csharppic = PhotoImage(file=csharppath)


# subroutine that runs when myButton is pressed
def show():
	# choice.get() returns the string that is referenced by the string variable choice
	# the label myLabel is set to display this text.
	myLabel.config(text=choice.get())
	# depending on what this text is, the correct image is also added to the label
	# compound can be set to BOTTOM, TOP, LEFT or RIGHT.
	if choice.get() == "Python":
		myLabel.config(image=pythonpic, compound=BOTTOM)  # image is set to the bottom of the label
	elif choice.get() == "Java":
		myLabel.config(image=javapic, compound=BOTTOM)
	elif choice.get() == "C++":
		myLabel.config(image=cpluspic, compound=BOTTOM)
	elif choice.get() == "Javascript":
		myLabel.config(image=javascriptpic, compound=BOTTOM)
	elif choice.get() == "PHP":
		myLabel.config(image=phppic, compound=BOTTOM)
	elif choice.get() == "C#":
		myLabel.config(image=csharppic, compound=BOTTOM)


# creates variable used in drop down menu
choice = StringVar()
choice.set("Python")

# declare all the widgets and their parameters.
drop = OptionMenu(window, choice, "Python", "Java", "C++", "Javascript", "PHP", "C#")
myButton = Button(window, text="Show selection", command=show)
myLabel = Label(window)

# add the widgets to the window using the pack() layout manager.
drop.pack()
myButton.pack()
myLabel.pack()

#run window and listen for events.
window.mainloop()
