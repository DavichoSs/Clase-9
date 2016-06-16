from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

imagen=PhotoImage(file="logo.gif")
canvas.create_image(10,10, anchor=NW, image=imagen)
tk.mainloop()