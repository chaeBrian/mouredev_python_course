# Classes

# Definition

class EmptyClass:
    pass  # Para poder dejar la clase vacía

print(EmptyClass)
print(EmptyClass())


# Clase con constructor, functions, popiedades privadas y públicas

class Player:
    def __init__(self, name, surname, club="without club"):
        self.full_name = f"{name} {surname} ({club})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def playing(self):
        print(f"{self.full_name} is playing")


my_player = Player("Lionel", "Messi")
print(my_player.full_name)
print(my_player.get_name())
my_player.playing()

my_other_person = Player("Lionel", "Messi", "PSG")
print(my_other_person.full_name)
my_other_person.playing()
my_other_person.full_name = "Kai Havertz (Chelsea)"
print(my_other_person.full_name)

my_other_person.full_name = 141516
print(my_other_person.full_name)