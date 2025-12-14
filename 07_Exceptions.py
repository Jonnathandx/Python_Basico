number_1 = 5
number_2 = 3

number_2 = '3'

# try, except
try:
    number_1 + number_2
    print('No hay error')
except:
    print('Error')

# try, except, else

try:
    number_1 + number_2
    print('No hay error')
except:
    print('Error')
else:
    print('El programa continua ejecutandose correctamente')

# try, except, else, finally

try:
    number_1 + number_2
    print('No hay error')
except:
    print('Error')
else: # Opcional
    print('El programa continua ejecutandose correctamente')
finally: # Opcional
    # Se ejecuta siempre
    print('La ejecucion continua')