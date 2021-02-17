"""
This is a basic window that closes when the cross is pressed.
A frame class is created.  The base window is passed to this class.
A label is added to the frame
"""
import tkinter as tk


class ExampleFrame(tk.Frame):
	def __init__(self, the_window):
		super().__init__()  # this invokes the constructor of the super class Frame
		self["width"] = 300  # sets the width of the greenFrame instance to 300
		self["height"] = 300  # sets the height of the greenframe instance to 300
		self["relief"] = "sunken"  # sets the relief of the greenframe instance to sunken
		self["border"] = 8
		self["bg"] = "green"
		self["padx"] = 8
		self["pady"] = 125  # changing the value of the padx and pady will change the label position.
		self.addLabel()

		# this method creates a label and adds it to the frame.
	def addLabel(self):
		lbl_one = tk.Label(self,
		                   text="This is label one")  # self is passed to the label as the window it will be added to
		lbl_one.grid(row=0, column=0)


window = tk.Tk()  # creates new base window.

window.title("My window")
window.geometry("300x300")  # width x height

# creates an instance of the ExampleFrame class
a_frame = ExampleFrame(window)
# adds the frame to the base window
a_frame.grid(row=0, column=0)
window.mainloop()
