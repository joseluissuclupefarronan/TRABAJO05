#verificador N°04
#esta calculadora calcula el promedio de tres notas.

#declaracion de las variables
nota1,nota2,nota3,promedio=0.0,0.0,0.0,0.0

#calculadora
nota1=float(input("mostrar la nota 1"))
nota2=float(input("mostrar la nota 2"))
nota3=float(input("mostrar la nota 3"))
promedio=(nota1+nota2+nota3)/3
verificador=(promedio==11)

#mostrar datos
print("la nota 1 es=", nota1)
print("la nota 2 es=", nota2)
print("la nota 3 es=", nota3)
print("el promedio es:",promedio)
print("el promedio es==11", verificador)
