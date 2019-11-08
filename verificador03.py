#verificador N°03
#esta calculadora calcula el area de un triangulo.

#declaracion de las variables
base,altura,area_triangulo=0.0,0.0,0.0

#calculadora
base=int(input("mostrar la base"))
altura=int(input("mostrar la altura"))
area_triangulo=(base*altura)/2
verificador=(area_triangulo<=50)

#mostrar datos
print("la base es=", base)
print("la altura es=", altura)
print("el area del triangulo es:",area_triangulo)
print("el area del triangulo es<=50:", verificador)

