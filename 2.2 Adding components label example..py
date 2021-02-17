"""
This is a basic window that closes when the cross is pressed.
A frame is created and added to this base window.
"""
import tkinter as tk

window = tk.Tk()  # creates new base window.

window.title("My window")
window.geometry("300x300")  # width x height

# I have added padx and pady to this frame so that
# when the label is added it is in the middle of the frame.
# padding adds space inside the widget.
# if you remove this padding the frame will only be as big as
# the widgets added to it.
a_frame = tk.Frame(window,
                   width=300,
                   height=300,
                   bg="green",
                   bd=8,
                   relief="sunken",
                   padx=8,
                   pady=125)

# creating a label, passing it the base window.
lbl_myLabel = tk.Label(a_frame,
                       text="Hello this is a label",
                       padx=5,
                       pady=5)


# add the label to the frame and then the frame to the base window.
lbl_myLabel.grid(row=0, column=0)
a_frame.grid(row=0, column=0)


window.mainloop()  # event loop
