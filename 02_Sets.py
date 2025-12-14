my_set = set()
other_set = {}

print(type(my_set))
print(type(other_set))

other_set = {'Jonnathan', 'Nieves', 28, 1.78}

print(type(other_set))
print(other_set)

other_set.add('Developer')

print(other_set) # No es una estructura ordenada

other_set.add('Developer') # No admite repetidos

print(other_set)
