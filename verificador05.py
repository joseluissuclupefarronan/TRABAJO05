#verificador N°05
#esta calculadora calcula el perimetro de un triangulo.

#declaracion de las variables
lado1,lado2,lado3,perimetro_triangulo=0.0,0.0,0.0,0.0

#calculadora
lado1=int(input("mostrar el lado 1"))
lado2=int(input("mostrar el lado 2"))
lado3=int(input("mostrar el lado 3"))
perimetro_triangulo=(lado1+lado2+lado3)
verificador=(perimetro_triangulo<=50)


#mostrar datos
print("el lado 1 es=", lado1)
print("el lado 2 es=", lado2)
print("el lado 3 es=", lado3)
print("el perimetro del triangulo es:",perimetro_triangulo)
print("el perimetro del triangulo es>=50:", verificador)

