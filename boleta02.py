#input
Distancia=int(input("Distancia:"))
Tiempo=int(input("Tiempo:"))

#processing
Velocidad=(Distancia/Tiempo)
print("Velocidad:", Velocidad)

#verificador
comprobar=(Velocidad<=40)

#output
print("#############################################")
print("#   DISTANCIA RECORRIDA POR UN MOVIL        #")
print("#############################################")
print("# DATOS:                  VALOR:            #")
print("# Distancia:             ",Distancia,"                #")
print("# Tiempo:                ",Tiempo,"                # ")
print("# Velocidad:             ",Velocidad,"              #")
print("#############################################")
print(" comprobar la velocidad:", comprobar)

