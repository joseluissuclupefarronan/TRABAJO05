#intput
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
p=int(input("p:"))

#processing
A=(x*y)/z+p
print("A:",A)
#verificador
comprobar=(A==90)

#output
print("###############################")
print("#        CALCULAR A           #")
print("###############################")
print("#VARIABLES:         VALOR:    #")
print("# x:               ",x,"        #")
print("# y:               ",y,"        #")
print("# z:               ",z,"        #")
print("# p:               ",p,"        #")
print("# A:               ",A,"     #")
print("###############################")
print(" comprobar el valor de A:",comprobar)
