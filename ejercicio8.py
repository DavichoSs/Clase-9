from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

imagen=PhotoImage(file="fondo.gif")
canvas.create_image(0,0, anchor=NW, image=imagen)
canvas.create_image(10,10, anchor=NW, image=imagen)
canvas.create_image(20,20, anchor=NW, image=imagen)
canvas.create_image(30,30, anchor=NW, image=imagen)
canvas.create_image(40,40, anchor=NW, image=imagen)
canvas.create_image(50,50, anchor=NW, image=imagen)
tk.mainloop()