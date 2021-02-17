"""
choose a file to open.  This could be combined with file reading.
"""
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.filename = tk.filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))

print(root.filename)

root.mainloop()
