#verificador N°17
#esta calculadora calcula el area de un prisma cudrangular regular.

#declaracion de las variables
l,h,area=0.0,0.0,0.0,

#calculadora
l=int(input("ingrese el valor del lado del prisma cuadrangular"))
h=int(input("ingrese la altura"))
area=2*l*(l+(2*h))
verificador=(area==150)

#mostrar datos
print("el lado del cuadrado es=", l)
print("la altura del cuadrado es=",h)
print("el area del prisma cuadrangular regular es=", area)
print("el area es==150:", verificador)
