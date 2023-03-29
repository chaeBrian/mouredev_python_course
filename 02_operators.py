# Operadores

print(3 + 4) # suma
print(3 - 4) # resta
print(3 * 4) # multiplicacion
print(3 / 4) # division
print(10 % 3) # resto
print(10 // 3) # floor division
print(2 ** 3) # Exponenciación
print(2 ** 3 + 3 - 7 / 1 // 4)  # todos los operadores pueden combinarse sin ningun problema

print("Hola " + "Python " + "¿Que tal?") # Concatenacion de strings con signo +
print("Hola " * 5) # Multiplicacion de stringsm, se imprimira la cantidad de strings que solicite el multiplicador
# 'print("Hola " + 5)' esto se tomara como error, la forma correcta seria la siguiente
print("Hola " + str(5)) # Otro ejemplo seria 'print("Hola " + "5")'

print("Hola " * (2 ** 3))
# 'print("Hola " * (2.5 * 2))' jamas funcionaria, ya que (2.5 * 2) me dara un valor float, 5.0
# para resolverlo debo cambiar el tipo de float a int(2.5 * 2)


# Operadores comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Curiosidad*
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")
## Estas comparaciones se basan en un Orden Alfabetico por ASCII
## Para comparar cantidad de caracteres, debemos usar la funcion 'len'
print(len("Hola") >= len("Python"))


# Operadores Logicos

print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" > "Python")
print(3 > 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4)) # Sirmpre devolvera el booleano inverso
