from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

imagen=PhotoImage(file="ball.gif")
canvas.create_image(20,20, anchor=NW, image=imagen)
tk.mainloop()