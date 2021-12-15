
notaAlumno=input("Ingresa tu calificacion: ")

def valoracion(nota):
    valoracion="aprobado"

    if nota<5:
      valoracion="reprobado"

    return valoracion

print(valoracion(int(notaAlumno)))

