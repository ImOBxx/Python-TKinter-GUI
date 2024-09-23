import tkinter as tk

root = tk.Tk()
root.title("Pack Example")

b1 = tk.Button(root, text = "Button 1")
b2 = tk.Button(root, text = "Button 2")
b3 = tk.Button(root, text = "Button 3")

b1.pack()
b2.pack()
b3.pack()

root.mainloop()