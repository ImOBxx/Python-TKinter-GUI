
from tkinter import *

root = Tk()
root.geometry("300x200")  # Set the window size

# Explicitly set the application name (useful for macOS)
root.title("Tkinter App on Mac")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)

helpmenu.add_command(label='About')

root.mainloop()


"""

from tkinter import *

root = Tk()
root.geometry("300x200")  # Set the window size
label = Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)
root.mainloop()
"""