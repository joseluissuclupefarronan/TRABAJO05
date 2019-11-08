#intput
velocidad=int(input("velocidad:"))
fuerza=int(input("Fuerza:"))

#processing
potencia=fuerza*velocidad
print("Potencia:", potencia)

#verificador
comprobar=(potencia!=60)

#output
print("#####################################")
print("#      POTENCIA DE UN AUTO          #")
print("#####################################")
print("# DATOS:              VALOR:        #")
print("# velocidad:         ",velocidad,"            #")
print("# fuerza:            ",fuerza,"            #")
print("# potencia:          ",potencia,"           #")
print("#####################################")
print("comprobar la potencia de la grua:",comprobar)

