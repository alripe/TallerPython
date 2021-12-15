#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. 
#Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: 
# “Los datos personales son: nombre apellido teléfono” 
# (Se mostrarán los datos introducidos por teclado).

Nombre=input("Ingresa tu nombre:\n")
Direccion=input("Ingresa tu direccion:\n")
Tfno=input("Ingresa tu telefono\n")

datos=[Nombre,Direccion,Tfno]

#print(datos)

print("Los datos son:\n"+datos[0]+"\n"+datos[1]+"\n"+datos[2])

