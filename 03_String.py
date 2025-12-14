# Split

codigo = 'V-854127-8'

code_sep = codigo.split('-')
a = ''.join(code_sep[1:])
print(a)

# Inversion de cadena

frase = 'Desarrollo'
# Inversion [start:end:step]
reverse_phase = frase[::-1]
print(reverse_phase)

# Palindromo

palindromo = 'Reconocer'
palabra = palindromo[::-1].lower() == palindromo.lower()
print(palabra)

# Limpieza de espacios
cadena_sucia = ' Python es genial '
limpia = cadena_sucia.split()
print(' '.join(limpia))

# Frecuencia de caracteres
entrada = 'banana'
frecuencia = dict()
frecuencia_pro = dict()

for i in entrada:
    if i in frecuencia:
        frecuencia[i] += 1
    else:
        frecuencia[i] = 1

# Enmascarar informacion sensible

def enmascarar_datos(mail):
    try:
        usuario, dominio = mail.split('@')

        if len(usuario) <= 2:
            print('Usuario demasiado corto para enmascarar')

        else:
            user_mask = f'{usuario[0]}{'*' * (len(usuario) - 2)}{usuario[-1]}'
        
        return f'{user_mask}@{dominio}'
    except ValueError:
        return 'Email invalido'

entrada = 'jonnathan.nievesn@gmail.com'

print(enmascarar_datos(entrada))

