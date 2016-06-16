import turtle
def poligono(size,lado):
	t=turtle.Pen()
	for x in range(0,lado):
		t.forward(size)
		t.left(360/lado)
	turtle.getscreen()._root.mainloop()
a=int(input("Ingrese el tamaño(0-200): "))
b=int(input("Cuantos lados desea visualizar?: "))
poligono(a,b)
