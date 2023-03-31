### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [10, 35, "Lionel", "Messi"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Lionel"))

age, shirt_number, name, surname = my_other_list
print(name)

name, shirt_number, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("Argentina")
print(my_other_list)

my_other_list.insert(1, "PSG")
print(my_other_list)

my_other_list[1] = "Barcelona"
print(my_other_list)

my_other_list.remove("Barcelona")
print(my_other_list)

my_list.remove(35) # .remove elimina el elemente que le proporcionamos, sabien que esta en la lista
print(my_list)

print(my_list.pop()) # .pop elimina pero tambien retorna el elemento eliminado, es util cuando queremos conservar lo eliminado
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2] # del elimina el elemento situado en el indice indicado
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))