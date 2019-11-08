#verificador N°11
#esta calculadora calcula el perimetro de un poligono regular.

#declaracion de las variables
lad1,lad2,lad3,lad4,lad5,perimetro_poligono_regular=0.0,0.0,0.0,0.0,0.0,0.0

#calculadora
lad1=int(input("ingrese el lado 1"))
lad2=int(input("ingrese el lado 2"))
lad3=int(input("ingrese el lado 3"))
lad4=int(input("ingrese el lado 4"))
lad5=int(input("ingrese el lado 5"))
perimetro_poligono_regular=(lad1+lad2+lad3+lad4+lad5)
verificador=(perimetro_poligono_regular>=50)

#mostrar datos
print("el lado 1 es=", lad1)
print("el lado 2 es=", lad2)
print("el lado 3 es=", lad3)
print("el lado 4 es=", lad4)
print("el lado 5 es=", lad5)
print("el perimetro del poligono regular es:",perimetro_poligono_regular)
print("el perimetro del poligono regular es>=50:", verificador)
