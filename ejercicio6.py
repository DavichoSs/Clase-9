import turtle
def cuadrado(size):
	t=turtle.Pen()
	for x in range(1,5):
		t.forward(size)
		t.left(90)
	turtle.getscreen()._root.mainloop()
a=int(input("Ingrese un numero: "))
cuadrado(a)