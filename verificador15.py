#verificador N°15
#esta calculadora calcula el numero de aristas de un prisma triangular.

#declaracion de las variables
nro_aristas,vertice,caras=0.0,0.0,0.0

#calculadora
caras=int(input("ingrese el numero de caras"))
vertice=int(input("ingrese el vertice"))
nro_aristas=(caras+vertice)-2
verificador=(nro_aristas!=50)

#mostrar datos
print("el numero de caras es=",caras)
print("el numero de vertices es=",vertice)
print("el numero de aristas de un prisma triangular es=", nro_aristas)
print("el numero de aristas de un prisma triangular es!=50:",verificador)
