# Clase Docente hereda de Persona
from Persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, edad, direccion, cargo):
        super().__init__(nombre, edad, direccion)  # Llamamos al constructor de la clase base (Persona)
        self.__cargo = cargo  # Atributo específico de Docente

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    def __str__(self):
        return f"{super().__str__()}, Cargo: {self.cargo}"