#verificador N°09
#esta calculadora calcula el area de un pentagono.

#declaracion de las variables
apotema,base,perimetro_pentagono,area_pentagono=0.0,0.0,0.0,0.0

#calculadora
base=int(input("ingrese la base"))
apotema=int(input("ingrese el apotema"))
perimetro_pentagono=int(input("ingrese el perimetro del pentagono"))
area_pentagono=(perimetro_pentagono*apotema)/2
verificador=(area_pentagono!=65)

#mostrar datos
print("la base es=",base)
print("el apotema es=",apotema)
print("el perimetro es=",perimetro_pentagono)
print("el area del pentagono es:",area_pentagono)
print("el area del pentagono es!=65:", verificador)
