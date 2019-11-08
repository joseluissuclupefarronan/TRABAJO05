#verificador N°07
#esta calculadora calcula el perimetro de un trapecio.

#declaracion de las variables
lado1,lado2,lado3,lado4,perimetro_triangulo=0.0,0.0,0.0,0.0,0.0

#calculadora
lado1=int(input("mostrar el lado 1"))
lado2=int(input("mostrar el lado 2"))
lado3=int(input("mostrar el lado 3"))
lado4=int(input("mostrar el lado 4"))
perimetro_trapecio=(lado1+lado2+lado3+lado4)
verificador=(perimetro_trapecio<=20)

#mostrar datos
print("el lado 1 es=", lado1)
print("el lado 2 es=", lado2)
print("el lado 3 es=", lado3)
print("el lado 4 es=", lado4)
print("el perimetro del trapecio es:",perimetro_trapecio)
print("el perimetro del trapecio es<=20:",verificador)
