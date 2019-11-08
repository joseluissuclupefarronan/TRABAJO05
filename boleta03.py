#input
lad1=int(input("Lad1:"))
lad2=int(input("Lad2:"))
lad3=float(input("Lad3:"))

#processing
volumen=lad1*lad2*lad3
print("volumen:", volumen)

#verificador
comprobador=(volumen==20)

#uotput
print("#########################################")
print("#           VOLUMEN DE UN CUBO          #")
print("#########################################")
print("# DATOS:          VALOR:                #")
print("# lad1:          ",lad1,"                    #")
print("# lad2:          ",lad2,"                    #")
print("# lad3:          ",lad3,"                  #")
print("# volumen:       ",volumen,"                #")
print("#########################################")
print("comprobador del volumen:", comprobador)

