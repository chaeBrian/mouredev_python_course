# Variables

var_name = "Lionel"
var_surname = "Messi"
var_nationality = "Argentina"

# Concatenacion de variables en un 'print'

print(var_name, var_surname, "from", var_nationality)

# Algunas variables del sistema...

print(len(var_name)) # retorna la cantidad de caracteres dentro de una variable

# Variables en una sola linea de codigo

name, surname, nationality = "Lionel", "Messi", "Argentina"

print("My idol is", name, surname, "and he is from", nationality)

# Inputs

first_name = input("What is your name?")
age = input("How old are you?")

print(first_name)
print(age)

# Cambio de tipos, las variables se pisan
name = "Enzo"
surname = "Fernandez"

# Forzamos el tipo?

name = srt = "Brian"
name = True
name = 10
name = 10.5

print(name) # name va a imprimir 10.5 por ser el ultimo valor que recibe la variable
