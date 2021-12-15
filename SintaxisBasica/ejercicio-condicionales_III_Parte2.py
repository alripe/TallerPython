#programa que verifique si un alumno tiene derecho a beca


print("Ingresa la distancia a la que vives")
distancia=int(input("Ingresa el dato: "))

print("Ingresa la cantidad de hermanos que tienes")
hermanos=int(input("Ingresa el dato: "))

print("Ingresa el salario promedio de la familia")
salario=int(input("Ingresa el dato: "))


print("\ndistancia: "+distancia)
print("cantidad de hermanos: "+hermanos)
print("salario promedio: "+salario)

if distancia >40 and hermanos >4 and salario <=7000:
    print("Tienes derecho a beca")
else:
    print("No cumples con los requisitos para la beca")

    

