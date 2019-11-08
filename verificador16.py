#verificador N°16
#esta calculadora calcula el area de un prisma triangular regular.

#declaracion de las variables
lt,h,area=0.0,0.0,0.0

#calculadora
lt=int(input("ingrese el lado del triangulo"))
h=int(input("ingrese la altura del triangulo"))
raiz=1.73205
area=(lt*(raiz/2)*lt + (3*h))
verificador=(area>=40)

#mostrar datos
print("el lado del triangulo es=",lt)
print("la altura del triangulo es=",h)
print("el area del prisma triangular es=", area)
print("el area es>=40:", verificador)
