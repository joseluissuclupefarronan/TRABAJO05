#input
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))

#processing
S=(a/b)*(c/d)
print("s:",S)

#verificador
comprobar=(S>=30)

#output
print("###############################")
print("#    CALCULAR EL VALOR S      #")
print("###############################")
print("#VARIABLES:          VALOR:   #")
print("# a:                  ",a,"     # ")
print("# b:                  ",b,"     #")
print("# c:                  ",c,"     #")
print("# d:                  ",d,"     #")
print("# s:                  ",S,"   #")
print("###############################")
print("comprobar el valor de S:",comprobar)
