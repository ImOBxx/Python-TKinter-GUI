from tkinter import *

top = Tk()

lb = Listbox(top)

lb.insert(1, 'Python')
lb.insert(1, 'Java')
lb.insert(1, 'C++')
lb.insert(1, 'Any Other')
lb.pack()



top.mainloop()