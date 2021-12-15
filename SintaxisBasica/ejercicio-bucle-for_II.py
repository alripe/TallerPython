#Programa que pueda evaluar si un email es correcto

emailValoracion=0
email = input("Ingresa tu email: ")


for i in email:
    if i=="@" or i==".":
        emailValoracion+emailValoracion+1
    

if emailValoracion==2:
    print("El correo es correcto")
else:
    print("El correo no es correcto")



