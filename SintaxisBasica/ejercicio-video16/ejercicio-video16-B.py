contador=0
password = input("Ingresa la contrasena: ")

for i in range(len(password)):
    if password[i]==" ":
        contador=1
         

if len(password)<8 or contador==1:
    print(" La contrasena no es correcta")

    print(list(password))
else:
    print("La contrasena es correcta")
