#verificador N°19
#esta calculadora calcula el volumen de una esfera.

#declaracion de las variables
radio,pi,volumen=0.0,0.0,0.0

#calculadora
radio=int(input("ingrese el radio"))
pi=3.141592
volumen=((4/3)*pi*(radio**3))
verificador=(volumen<=945)

#mostrar datos
print("el radio es=", radio)
print("el valor de pi es=",pi)
print("el volumen de la esfera es=", volumen)
print("el volumen de una esfera es<=945:",verificador)
