#Crea un programa que pida dos números por teclado. 
# El programa tendrá una función llamada “DevuelveMax” 
# encargada de devolver el número más alto de los dos introducidos.

numA = int(input("Ingresa el primer numero:"))

numB = int(input("Ingresa el segundo numero"))


def DelvuelveMax (nA, nB):

    if nA < nB:
        print("El segundo numero es mas alto")
    elif(nA > nB):
        print("El primer numero es mas alto")
    else:
        print("Los Numeros son iguales")
    
DelvuelveMax(numA, numB)



    