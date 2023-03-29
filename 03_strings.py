# Strings

my_string = "My string"
my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))

print(len(my_string + " " + my_other_string))

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Lionel", "Messi", 35

# %s espera recibir un string, %d en cambio espera un numero

print("Su nombre es {} {} y su edad es {}". format(name, surname, age))
print("Su nombre es %s %s y su edad es %d" %(name, surname, age)) # Definir el tipo de dato
print("Su nombre es " + name + " " + surname + " y su edad es " + str(age)) # Esta forma no es buena practica como las otras dos

print(f"Su nombre es {name} {surname} y su edad es {age}") # Si la idea es pasar los datos tal cual, esta es la mejor forma

# Desempaquetado de caracteres

language = "Python"
# a, b = "lenguage"  / esto dara error
a, b, c, d, e, f = language # en cambio este formato, me permite mostrar cada letra de la variable

# Division

language_slice = language[1-3]
print(language_slice) # esto me imprime las letras de la variable que se encuentren dentro del numero de caracteres que especifico
language_slice = language[0:6:2] # esto me imprimira los caracteres fijos en sus respectivas posiciones numeradas
print(language_slice)

# Reverse

reversed_language = language[::-1] # Imprime al reverso

# Funciones

my_nationality = "argentina"

print(my_nationality.capitalize()) # Imprime la primer letra en mayuscula
print(my_nationality.upper()) # Imprime la variable en Mayuscula
print(my_nationality.count("a")) # Imprime el conteo total de caracteres iguales, segun lo que este buscando
print(my_nationality.isnumeric()) # booleano para identificar numeros
print("1".isnumeric())
print(my_nationality.lower()) # imprime la variable en minusculas

print(my_nationality.lower().isupper()) # Concatenacion de funciones, en este ejemplo, uso la funcion de minusculas y luego la funcion para detectar mayusculas


