#intput
o=int(input("o:"))
p=int(input("p:"))
m=int(input("m:"))
l=int(input("l:"))
w=int(input("w:"))

#processing
z=((o*p)+(m-l))/w

#verificador
comprobar=(z<=2.504)

#output
print("##################################")
print("#   CALCULAR EL VALOR Z          #")
print("##################################")
print("# VARIABLES:          VALOR:     #")
print("# o:                 ", o ,"         #")
print("# p:                 ", p ,"         #")
print("# m:                 ", m ,"         #")
print("# l:                 ", l ,"         #")
print("# w:                 ", w ,"         #")
print("# z:                 ", z ,"       #")
print("##################################")
print(" comrobar el valor de G:", comprobar)
