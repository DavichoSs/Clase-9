import turtle
a=int(input("Ingrese un numero: "))
t=turtle.Pen()
t.speed(1)
for x in range(0,a):
	t.speed(1)
	t.forward(100)
	t.left(360/a)
for x in range(0,a):
	t.speed(1)
	t.forward(100)
	t.right(360/a)
turtle.getscreen()._root.mainloop()