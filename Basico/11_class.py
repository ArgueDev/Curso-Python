# Clases #

class Person:
    pass

print(Person())
print(Person)

class Persona:
    def __init__(self, name, surname, alias = '{Sin alias}'):
        self.__name = name # Propiedad Privada
        self.__surname = surname # Propiedad Privada
        self.full_name = f'{name} {surname} {alias}' # Propiedad Publica

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname
    def walk(self):
        print(f'{self.full_name} esta caminando')

persona = Persona('Christian', 'Arguello')
print(persona.get_name())
print(persona.get_surname())
print(persona.full_name)
persona.walk()

persona2 = Persona('Rene', 'Mera', 'ArgueDev')
print(persona2.full_name)
persona2.walk()