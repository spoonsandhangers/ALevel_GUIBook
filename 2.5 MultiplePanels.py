"""
This is a basic window that closes when the cross is pressed.
2 frames are created and added to this base window.
"""
import tkinter as tk

window = tk.Tk()  # creates new base window.

window.title("My window")
window.geometry("600x300")  # width x height


a_frame = tk.Frame(window,
                   width=300,
                   height=300,
                   bg="green",
                   bd=8,
                   relief="sunken")

b_frame = tk.Frame(window,
                   width=300,
                   height=300,
                   bg="red",
                   bd=8,
                   relief="sunken")


#  this adds this frame to the base window.
a_frame.grid(row=0, column=0)
b_frame.grid(row=0, column=1)


window.mainloop()  # event loop
