#intput
F=int(input("Fuerza:"))
D=int(input("Distancia:"))

#processing
Trabajo=F*D
print("Tabajo:",Trabajo)

#verificador
comprobar=(Trabajo==80)

#output
print("###############################################")
print("# TRABAJO QUE REALIZA UNA PERSONA A UN OBJETO #")
print("###############################################")
print("# DATOS:               VALOR:                 #")
print("# Fuerza:              ",F,"                    #")
print("# Distancia:           ",D,"                    #")
print("# Trabajo:             ",Trabajo,"                   #")
print("###############################################")
print(" comprobar el trabajo:", comprobar)
