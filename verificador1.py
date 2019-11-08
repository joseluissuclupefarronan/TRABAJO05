#verificador N°01
#esta calculadora calcula la velocidad final de un movil.

#declaracion de las variables
v_inicial,aceleracion,tiempo,v_final=0.0,0.0,0.0,0.0

#calculadora
v_inicial=int(input("mostrar la velocidad inicial"))
aceleracion=int(input("mostrar la aceleracion"))
tiempo=int(input("mostar el tiempo"))
v_final=(v_inicial+aceleracion)*tiempo
verificador=(v_final>=155)

#mostrar datos
print("la velocidad inicial es=", v_inicial)
print("la aceleracion es=", aceleracion)
print("el tiempo es=", tiempo)
print("la velocidad final del movil es=", v_final)
print("velocidad final==155:" ,  verificador)

