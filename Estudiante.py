# Clase Estudiante hereda de Persona
from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, semestre):
        super().__init__(nombre, edad, direccion)  # Llamamos al constructor de la clase base (Persona)
        self.__semestre = semestre  # Atributo específico de Estudiante

    @property
    def semestre(self):
        return self.__semestre

    @semestre.setter
    def semestre(self, semestre):
        self.__semestre = semestre

    def __str__(self):
        return f"{super().__str__()}, semestre: {self.semestre}"


