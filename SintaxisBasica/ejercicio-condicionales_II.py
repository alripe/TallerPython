#ejercicio de condicionales
print("Programa para calcular las calificaciones de un estudiante")

calificacion=int(input("Ingresas tu calificacion: "))

if calificacion<5:
    print("la calificacion es insufuciente")

elif calificacion<6:
    print("la caificacion es suficiente")
elif calificacion<7:
    print("la calificacion es apta")
elif calificacion<8:
    print("buen trabajo")
elif calificacion<9:
    print("fantastico trabajo continua asi")
elif calificacion<10:
    print("la gloria te espera, no hay mas que decir")
else:
    print("error al teclear la calificacion")
 