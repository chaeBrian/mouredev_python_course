# Dictionaries

#Definicion

my_dict = dict()
my_other_dict = {}

# Un diccionario en Python se compone de un conjunto en formato clave-valor. Estas claves pueden ser 'string' o 'number'.
my_other_dict = {
    "Name": "Lionel",
    "Surname": "Messi",
    "Nationality": "Argentina"
}
# Los valores, pueden ser tanto un 'boolean', 'string', 'number', etc; Como asi tambien un 'set', 'list', 'tuple'..
my_dict = {
    "Name": "Lionel",
    "Surname": "Messi",
    "Nationality": "Argentina",
    "Clubs": {"Barcelona", "PSG"} 
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Busqueda

print(my_dict[1])
print(my_dict["Name"])