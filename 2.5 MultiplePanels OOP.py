"""
This is a basic window that closes when the cross is pressed.
This is expressed using a class.
As this is a class we can create more than one instance of it if we want to.
This code creates 2 MultiFrame panels and adds them both to the base window.
"""
# This import statement imports tkinter as tk
# each time we use a tkinter element we must add tk. in front of it
# this is much better practice as it does not contaminate the namespace.
import tkinter as tk


# a class called MultiFrame that inherits from Frame
# it also calls the super constructor.
# it sets the  attributes of the frame.
class MultiFrame(tk.Frame):
	def __init__(self, the_window, colour):
		super().__init__()  # this invokes the constructor of the super class Frame
		self["width"] = 300  # sets the width of the greenFrame instance to 300
		self["height"] = 300  # sets the height of the greenframe instsance to 300
		self["relief"] = "sunken"  # sets the relief of the greenframe instance to sunken
		self["border"] = 8
		self["bg"] = colour


window = tk.Tk()  # creates new base window.
window.title("Basic window")  # sets the title of this window

a_frame = MultiFrame(window, "green")
b_frame = MultiFrame(window, "red")  # creates a new instance of the class MultiFrame

a_frame.grid(row=0, column=0)  # Adds this instance to the base window
b_frame.grid(row=0, column=1)

window.mainloop()  # event loop
