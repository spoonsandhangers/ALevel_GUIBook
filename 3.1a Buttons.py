"""
Label widgets added to Frames.
padx and pady are parameters that set the interior distance from text in a label to the edge of the label.
when used in a frame it sets the distance from the edges of the frame to the internal widgets.
Buttons have the attribute command.  Whatever this equals should have a subroutine/method written with the same name.
The button defined here has command=clickMe.  The method clickMe(self) will run when this button is clicked
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
		self["padx"] = 80
		self["pady"] = 100  # changing the value of the padx and pady will change the label position.
		self.lbl_one = tk.Label(self,
		                   text="This is label one",
		                   font=("comic sans",10,"bold"),
		                   fg="white",
		                   bg="black",
		                   padx=5,
		                   pady=5)  # self is passed to the label as the window it will be added to
		self.lbl_two = tk.Label(self,
		                   text="This is label two",
		                   fg="purple",
		                   bg="white",
		                   font=("helvetica",20,"italic"),  # name a font, size and type
		                   padx=5,
		                   pady=5)
		self.lbl_three = tk.Label(self,
		                     text="This is label three",
		                     fg="blue",
		                     bg="yellow",
		                     font=("ariel",15),
		                     padx=5,
		                     pady=5)
		self.btn_one = tk.Button(self, command=self.clickMe, text="Click to change the text")
		self.addLabel()
		self.addButton()

		# this method creates labels and adds to them the frame self.

	def addLabel(self):
		self.lbl_one.grid(row=0, column=0)
		self.lbl_two.grid(row=1, column=0)
		self.lbl_three.grid(row=2, column=0)

	def addButton(self):
		self.btn_one.grid(row=3, column=0)

	def clickMe(self):
		self.lbl_one.config(text="Text changed on Label 1")
		self.lbl_two.config(text="Text changed on label 2")
		self.lbl_three.config(text="Text changed on label 3")



window = tk.Tk()  # creates new base window.

window.title("My window")
#window.geometry("300x300")  # width x height

# creates an instance of the ExampleFrame class
a_frame = ExampleFrame(window)
# adds the frame to the base window
a_frame.grid(row=0, column=0)
window.mainloop()
