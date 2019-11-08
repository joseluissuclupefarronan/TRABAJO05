#verificador N°10
#esta calculadora calcula el area de un exagono.

#declaracion de las variables
apotema,base,perimetro_exagono,area_exagono=0.0,0.0,0.0,0.0

#calculadora
base=int(input("ingrese la base"))
apotema=int(input("ingrese el apotema"))
perimetro_exagono=int(input("ingrese el perimetro del exagono"))
area_exagono=(perimetro_exagono*apotema)/2
verificador=(area_exagono==40)

#mostrar datos
print("la base es=",base)
print("el apotema es=",apotema)
print("el perimetro es=",perimetro_exagono)
print("el area del exagono es:",area_exagono)
print("el area del exagono es==40:",verificador)
