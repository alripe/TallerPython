
print("Ingresa la asignatura que elegiras como optativa")

opcion=input("Pruebas de Software\n""Bases de Datos\n""administracion de redes\n""-> ")
asignatura=opcion.lower()

if asignatura in ("pruebas de software","bases de datos","admisntracion de redes"):
    print("La asignatura seleccionada es: " +asignatura)
else:
    print("esta asignatura no existe")



