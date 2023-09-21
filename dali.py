'''
Desarrollar un programa en python que lea un número entero y 
muestre un mensaje indicando si el número leido ES o NO
múltiplo de 3

Desarrollar un programa en python que lea un número entero y 
muestre un mensaje indicando si el número leido es POSITIVO o
NEGATIVO

Desarrollar un programa en python que lea un número entero y 
muestre un mensaje indicando si el número leido corresponde 
o no a un mes de nuestro calendario (Desde 1 hasta 12)

'''
num = int(input("Por favor digite un número: "))
if num%3==0:
    print("ES multiplo de 3")
else:
    print("NO es múltiplo de 3")

num = int(input("Por favor digite un número: "))
if num<0:
    print("ES NEGATIVO")
else:
    print("ES POSITIVO")

num = int(input("Por favor digite un número: "))
if num<1 or num>12:
    print("NO ES UN MES")
else:
    print("ES UN MES DE NUESTRO CALENDARIO")
