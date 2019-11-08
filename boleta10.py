#intput
velocidad1=int(input("velocidad 1:"))
velocidad2=int(input("velocidad 2:"))
Distancia=int(input("Distancia:"))

#processing
Tiempo_alcance=Distancia/(velocidad1-velocidad2)
print("tiempo de alcance:",Tiempo_alcance)

#verificador
comprobar=(Tiempo_alcance>=60)

#output
print("###############################################")
print("# EL TIEMPO DE ALCANCE ENTRE DOS MOVILES      #")
print("###############################################")
print("# DATOS:               VALOR:                 #")
print("# velocidad 1:         ",velocidad1,"                   #")
print("# velocidad 2:         ",velocidad2,"                   #")
print("# Distancia:           ",Distancia,"                   #")
print("# tiempo de alcance:           ",Tiempo_alcance,"          #")
print("###############################################")
print(" comprobar el tiempo de alcance:", comprobar)

