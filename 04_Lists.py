# Manipulación Básica (Stack vs Queue)

tareas = ["Revisar correo", "Programar", "Llamar cliente", "Actualizar Jira"]

if 'Revisar correo' in tareas:
    tareas.remove('Revisar correo')

tarea_eliminada = tareas.pop()

tareas.insert(1, "Reunión diaria")

# List Comprehensions

# Pares
nums = [2, 6, 7, 9, 34, 89]

pares = [i for i in nums if i % 2 == 0]

# Filtrado y Transformación
precios_brutos = [10, 55, 100, 20, 200, 45]

precio_final = [round(j*1.15, 2) for j in precios_brutos if j > 50]

# Iteración Paralela (zip)
productos = ["Laptop", "Mouse", "Teclado"]
stock = [5, 20, 10]

inventario = list(zip(productos, stock))

for can, pro in zip(stock, productos):
    print(f'Existen {can} unidades de {pro}.')

# Ordenamiento Avanzado (Lambda Keys) Ordenar Usuarios por Edad

usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Beto", "edad": 19},
    {"nombre": "Carla", "edad": 30}
]

usuarios.sort(key=lambda u: u['edad'])

# Desempaquetado (Unpacking) Avanzado

participantes = ["Juan", "Pedro", "Maria", "Sofia"]

lider, *equipo = participantes

