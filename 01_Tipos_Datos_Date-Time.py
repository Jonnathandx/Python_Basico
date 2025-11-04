# Datetime
import datetime

# Fecha y hora actual
date_hour = datetime.datetime.now()
print(f'Fecha y hora actual: {date_hour}')

# Obtener solo la fecha actual
date = datetime.date.today()
print(f'La fecha actual es: {date}')

# Crear un objeto datetime especifico
datetime_specific = datetime.datetime(2020, 12, 12, 15, 30, 14)
print(f'Fecha y hora especifica: {datetime_specific}')

# Formatear la fecha y hora como una cadena
date_formated = date_hour.strftime('%Y-%m-%d %H-%M-%S')
print(date_formated)

# Obtener el anio actual
actual_year = date_hour.year
print(f'El anio actual es: {actual_year}')