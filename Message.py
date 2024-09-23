from tkinter import * 

main = Tk()

ourMessage = 'This is out Message'

messageVar = Message(main, text = ourMessage)

messageVar.config(bg='lightgreen')

messageVar.pack()

main.mainloop()

