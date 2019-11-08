#verificador N°12
#esta calculadora calcula el tiempo de encuentro entre dos moviles.

#declaracion de las variables
velocidad2,distacia,velocidad1,tiempo_encuentro=0.0,0.0,0.0,0.0

#calculadora
velocidad1=int(input("ingrese la velocidad 1"))
velocidad2=int(input("ingrese la velocidad 2"))
distacia=int(input("ingrese la distancia"))
tiempo_encuentro=(distacia)/velocidad1+velocidad2
verificador=(tiempo_encuentro!=70)

#mostrar datos
print("la velocidad 1 es=", str(velocidad1) + " mtr/s")
print("la velocidad 2 es=", str(velocidad2)+ " mtr/s")
print("la distancia es=",str(distacia) + " metros")
print("el tiempo de encuentro es en=", str(tiempo_encuentro) + " minutos")
print("el tiempo de encuentro es!=70:", verificador)
