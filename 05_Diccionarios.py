# Acceso Seguro de Datos - Configuración de Usuario

config = {"volumen": 50, "idioma": "es"}
tema = config.get('tema', 'light')

# Iteración Eficiente - Reporte de Inventario

precios = {"manzana": 1.5, "banana": 0.8, "kiwi": 2.0}

for i, j in precios.items():
    print(f'El precio de {i} es ${j}')

# Dictionary Comprehensions - Invertir un Diccionario

usuarios = {101: "Juan", 102: "Maria", 103: "Pedro"}
users_change = {nombre: id_user for id_user, nombre in usuarios.items()}

# Fusión de Diccionarios - Configuración por Defecto + Override
defaults = {"host": "localhost", "port": 8000, "debug": False}
user_cfg = {"port": 9090, "debug": True}

config_final = defaults | user_cfg

# Agrupación con defaultdict - Agrupar palabras por letra inicial
from collections import defaultdict

palabras = ["manzana", "banana", "mango", "cereza", "baya"]

salida = defaultdict(list)

for p in palabras:
    salida[p[0]].append(p)

print(dict(salida))

# Creacion de diccionario
my_dict = dict()

keys = ['Name', 'Cedula', 'Pais', 'Edad']

print(my_dict.fromkeys(keys, 'tzury'))

# Funciones

def suma_two_values(a:int, b: int):
    return a + b

suma_two_values(5, 7)