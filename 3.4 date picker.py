"""
This code shows a calendar and allows the user to select a date.
to use this you must first install the tkcalendar module
from the command line or shell in thonny type:
pip install tkcalendar
"""
import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Date picker")

cal = Calendar(root, selectmode= "day",
               year=2020,
               month = 2,
               day=15)

cal.pack()

def my_date():
	lbl_dateDisplay.config(text= "Selected date is: " + cal.get_date())


btn_dateDisplay = tk.Button(root, text="Get date",
                            command=my_date)

lbl_dateDisplay = tk.Label(root)

cal.pack()
btn_dateDisplay.pack()
lbl_dateDisplay.pack()

root.mainloop()

