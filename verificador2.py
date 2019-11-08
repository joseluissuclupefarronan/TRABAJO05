#verificador N°02
#esta calculadora calcula la aceleracion media de un movil.

#declaracion de las variables
velocidad1,velocidad2,tiempo,aceleracion_media=0.0,0.0,0.0,0.0

#calculadora
velocidad2=int(input("mostrar la velocidad 2"))
velocidad1=int(input("mostrar la velocidad 1"))
tiempo=int(input("mostrar el tiempo"))
aceleracion_media=((velocidad2-velocidad1)/tiempo)
verificador=(aceleracion_media==100)

#mostrar datos
print("la velocidad 1 es="+ str(velocidad1) + " km/h")
print("la velocidad 2 es="+ str(velocidad2) + " km/h")
print("el tiempo es=", str(tiempo) + " minutos")
print("La aceleracion media es:"+ str(aceleracion_media) + " km/h")
print("aceleracion media==100:", verificador)
