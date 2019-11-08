#intput
y=int(input("y:"))
z=int(input("z:"))

#processing
x=((y**2)+(z**2)+(y*z)+(y*z))
print("x:", x)

#verificador
comprobar=(x>=55.5)

#output
print("################################")
print("#         CALCULAR  x          #")
print("################################")
print("#VARIABLES:          VALOR:    #")
print("#y:                  ",y ,"       #")
print("#z:                  ",z,"       #")
print("#x:                   ",x,"    #")
print("################################")
print("comprobar la variable x:", comprobar)
