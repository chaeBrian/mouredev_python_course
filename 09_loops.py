# Loops

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Este metodo es opcional
    print("Mi condicion es igual o mayor a 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break # Break detiene mi ejecucion, evitando que en este caso se ejecute 'print(my_condition)'
        print(my_condition)

print("La ejecucion continua")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (10, "Argentina", "Messi", "Lionel")

for element in my_tuple:
    print(element)

my_set = {"Messi", "Lionel", 10}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Lionel", "Apellido": "Messi", "Edad": 35, 1: "10"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")