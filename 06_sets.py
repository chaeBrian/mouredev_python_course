# Sets

# Definicion

my_set = set()
print(type(my_set)) # <class 'set'>

my_other_set = {}
print(type(my_other_set)) # <class 'dict'>

my_other_set = {"Trezeguet", "Messi", "Henry"}
print(type(my_other_set)) # <class 'set'>

print(len(my_other_set)) # su longitud en este caso es 3
# print(my_other_set[0]) # pero si quisiera imprimir uno de sus elementos, almenos esta no es un forma de hacerlo.

# Insercion

my_other_set.add("Drogba") # agregamos un elemento al set
print(my_other_set) # como vemos un set no es una estructura ordenada, los elementos no tienen una posicion fija.

my_other_set.add("Drogba") # un set no admite repetidos.
print(my_other_set)


# Busqueda

print("Messi" in my_other_set) # esta es una forma de buscar elementos en nuestro set.
print("Mesi" in my_other_set)  # nos imprimira un boolean


# Eliminacion

my_other_set.remove("Drogba") # podemos borrar elementos, como en lists y tuples.
print(my_other_set)

my_other_set.clear() # borra completamente todo lo que contenga nuestro set.
print(my_other_set)

del my_other_set # borra directamente nuestro set, a diferencia de clear que solo borra su contenido.
# print(my_other_set) | nos arrojara un error, ya que 'my_other_set' ya noe existe.


# Transformacion.
my_set = {"Trezeguet", "Lionel", "Henry"}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # Hacer este tipo de transformaciones no es recomandado, ya que mi lista no se imprimira siempre igual. Por ende el elemento[0] no sera siempre el mismo.

my_other_set = {"DeBruyne", "Kraneviter", "Palacios"}


# Otras Operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Ronaldo", "Zidane"}))
# En este caso vemos que a pesar de usar 'union' los elementos de 'my_new_set' y 'my_set' no vuelven a agregarse.
# esto es basicamente porque un set no admite duplicados. En cambio en el tercer 'union', estos si se agregan facilmente.

print(my_new_set.difference(my_set))
# Difference se utiliza para encontrar la diferencia entro dos o mas conjuntos.
# Devolvera un nuevo conjunto que contenga elementos del resto de juntos a exepcion de en este caso 'my_set'. 
