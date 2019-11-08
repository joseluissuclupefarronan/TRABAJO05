#verificador N°18
#esta calculadora calcula el volumen de un cono.

#declaracion de las variables
radio,h_cono,pi,volumen=0.0,0.0,0.0,0.0

#calculadora
radio=int(input("ingrese el radio"))
h_cono=int(input("ingrese la altura del cono"))
pi=3.141592
volumen=((1/3)*pi*(radio*radio)*h_cono)
verificador=(volumen!=40)

#mostrar datos
print("el radio es=", radio)
print("la altura del cono es=",h_cono)
print("el volumen del cono es=", volumen)
print("el volumen del cono es!=70:",verificador)
