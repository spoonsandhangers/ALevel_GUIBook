"""
This is a basic window that closes when the cross is pressed.
A frame is created and added to this base window.
"""
# This import statement imports tkinter as tk
# each time we use a tkinter element we must add tk. in front of it
# this is much better practice as it does not contaminate the namespace.
import tkinter as tk

window = tk.Tk()  # creates new base window.

window.title("My window")
window.geometry("600x600")  # width x height

# creates a new frame with the same size as the base window.
# a green background colour, border of 8 pixels with a sunken relief.
# the first parameter passed to this is the base window as this is the
# window we want the frame to be associated with.
a_frame = tk.Frame(window,
                   width=300,
                   height=300,
                   bg="green",
                   bd=8,
                   relief="sunken")

#  this adds this frame to the base window.
a_frame.grid(row=0, column=0)

window.mainloop()  # event loop
