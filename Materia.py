# Clase Materia

class Materia:
    def __init__(self, nombre, docente=None):
        self.__nombre = nombre
        self.__docente = docente
        self.__estudiantes = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def docente(self):
        return self.__docente
    
    @docente.setter
    def docente(self, docente):
        self.__docente = docente
    
    @property
    def estudiantes(self):
        return self.__estudiantes
    
    def asignar_docente(self, docente):
        self.docente = docente
    
    def matricular_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)
    
    def __str__(self):
        estudiantes_str = "\n".join([f"- {est.nombre}" for est in self.__estudiantes]) if self.__estudiantes else "No hay estudiantes matriculados"
        return f"Materia: {self.nombre}\nDocente: {self.docente.nombre if self.docente else 'No asignado'}\nEstudiantes matriculados: {len(self.estudiantes)}\n{estudiantes_str}"
