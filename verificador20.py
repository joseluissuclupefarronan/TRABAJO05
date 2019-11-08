#verificador N°20
#esta calculadora calcula el volumen del ortoedro.

#declaracion de las variables
longitud,latitud,altura,volumen=0.0,0.0,0.0,0.0

#calculadora
longitud=int(input("ingrese la longitud"))
latitud=int(input("ingrese la latitud"))
altura=int(input("ingrese la altura"))
volumen=longitud*latitud*altura
verificador=(volumen==140)

#mostrar datos
print("la longitud es=", longitud)
print("la latitud es=",latitud)
print("la altura es=", altura)
print("el volumen del ortoedro es=", volumen)
print("el volumen del ortoedro es==140:",verificador)
