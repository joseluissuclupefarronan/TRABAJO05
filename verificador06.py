#verificador N°06
#esta calculadora calcula el area de un rombo.

#declaracion de las variables
diagonal_mayor,diagonal_menor,area_rombo=0.0,0.0,0.0

#calculadora
diagonal_mayor=int(input("mostrar la diagonal mayor"))
diagonal_menor=int(input("mostrar la diagonal menor"))
area_rombo=(diagonal_mayor*diagonal_menor)/2
verificador=(area_rombo!=60)

#mostrar datos
print("el valor de la diagonal mayor es=",diagonal_mayor)
print("el valor de la diagonal menor es=",diagonal_menor)
print("el area del rombo es:",area_rombo)
print("el area del rombo es!=60:",verificador)
