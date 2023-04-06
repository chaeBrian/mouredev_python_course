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

# 'print(my_dict)'
print(my_dict["Name"])
print("Messi" in my_dict)
print("Username" in my_dict)

# Inserción

my_dict["S-Number"] = 10
print(my_dict)

# Actualización

my_dict["Name"] = "Lionel Andres"
print(my_dict["Name"])

# Eliminación

del my_dict["S-Number"]
print(my_dict)

# Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Name", 10, "Nationality"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Name", 10, "Nationality"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "PSG")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))