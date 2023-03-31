### Tuples ###

# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (10, 35, "Lionel", "Andres", "Messi")
my_other_tuple = ("PSG", "Barcelona", "Newels")

print(my_tuple)
print(type(my_tuple))

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Lionel"))
print(my_tuple.index("Messi"))
print(my_tuple.index("Andres"))

# my_tuple[1] = 25 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista, haciendo esto podemos modificar la tupla. al finalizar la modificacion podemos revertir su estado a tupla.

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Argentina"
my_tuple.insert(1, "zurdo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple 
# En las tuplas no existe el Clear de las listas, y usando Del lo unico que haremos sera eliminar la tupla, tampoco podemos eliminar elementos de la tupla con del.
# print(my_tuple) NameError: name 'my_tuple' is not defined
