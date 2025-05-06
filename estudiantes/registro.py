import csv

def cargar_estudiantes(nombre_archivo):
    estudiantes = []
    with open(nombre_archivo, mode='r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                nombre = fila['nombre']
                nota = float(fila['nota'])
                if 0.0 <= nota <= 5.0:
                    estudiantes.append({'nombre': nombre, 'nota': nota})
            except ValueError:
                continue  
    return estudiantes
