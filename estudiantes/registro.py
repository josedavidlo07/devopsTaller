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

def mostrar_tabla(estudiantes):
    estudiantes.sort(key=lambda x: x['nombre'])
    print(f"{'Nombre':<20} {'Nota'}")
    print("-" * 30)
    for estudiante in estudiantes:
        print(f"{estudiante['nombre']:<20} {estudiante['nota']:.2f}")

def calcular_promedio(estudiantes):
    if not estudiantes:
        print("No hay estudiantes válidos.")
        return
    promedio = sum(est['nota'] for est in estudiantes) / len(estudiantes)
    print(f"\nPromedio general de notas: {promedio:.2f}")


