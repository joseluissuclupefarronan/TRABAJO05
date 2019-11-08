#verificador N°08
#esta calculadora calcula el area de un trapecio.

#declaracion de las variables
base_mayor,base_menor,altura,area_trapecio=0.0,0.0,0.0,0.0

#calculadora
base_mayor=int(input("mostrar la base mayor"))
base_menor=int(input("mostrar la base menor"))
altura=int(input("mostrar la altura"))
area_trapecio=((base_mayor+base_menor)*altura)/2
verificador=(area_trapecio==60)

#mostrar datos
print("la altura es=",altura)
print("la base mayor es=",base_mayor)
print("la base menor es=",base_menor)
print("el area del trapecio es:",area_trapecio)
print("el area del trapecio es==60:",verificador)
