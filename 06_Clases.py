class Persona:
    def __init__(self, first_name: str, last_name: str, age: int, country: str, mail: str, velocidad: int):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = f'{first_name} {last_name}'
        self.age = age
        self.country = country
        self.mail = mail
        self.velocidad = velocidad
    
    def correr(self, impulso):
        self.velocidad += impulso
        return self.velocidad
    
class Perro:
    def __init__(self, raza: str, edad: int, peso: float):
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def nadar(self):
        print('El perro esta nadando.')

# Objeto de la clase persona
my_person = Persona('Sara', 'Nambel', 3, 'Ecuador', 'tzura@gmail.com', 5)

print(f'{my_person.first_name} tiene {my_person.age} anios')

print(my_person.fullname)

print(my_person.correr(3))

# Objeto de la clase perro
my_dog = Perro('Labrador', 4, 15)

print(my_dog.edad)
my_dog.nadar()