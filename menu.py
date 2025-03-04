from Estudiante import Estudiante
from Docente import Docente
from Administrativo import Administrativo

class SistemaGestion:
    def __init__(self):
        self.estudiantes = []
        self.docentes = []
        self.administrativo = []

    ### 🔹 MÉTODOS PARA ESTUDIANTESs
    def agregar_estudiante(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        direccion = input("Ingrese la dirección del estudiante: ")
        semestre = input("Ingrese el semestre del estudiante: ")
        estudiante = Estudiante(nombre, edad, direccion, semestre)
        self.estudiantes.append(estudiante)
        print("\n✅ Estudiante agregado correctamente.\n")

    def listar_estudiantes(self):
        if not self.estudiantes:
            print("\n⚠️ No hay estudiantes registrados.\n")
        else:
            print("\n📋 Lista de estudiantes:")
            for idx, estudiante in enumerate(self.estudiantes, start=1):
                print(f"{idx}. {estudiante}")

    def modificar_estudiante(self):
        self.listar_estudiantes()
        if not self.estudiantes:
            return
        try:
            idx = int(input("\nIngrese el número del estudiante a modificar: ")) - 1
            if 0 <= idx < len(self.estudiantes):
                estudiante = self.estudiantes[idx]
                estudiante.nombre = input(f"Nuevo nombre ({estudiante.nombre}): ") or estudiante.nombre
                estudiante.edad = int(input(f"Nueva edad ({estudiante.edad}): ") or estudiante.edad)
                estudiante.direccion = input(f"Nueva dirección ({estudiante.direccion}): ") or estudiante.direccion
                estudiante.semestre = input(f"Nuevo semestre ({estudiante.semestre}): ") or estudiante.semestre
                print("\n✅ Estudiante modificado correctamente.\n")
            else:
                print("\n⚠️ Número inválido.\n")
        except ValueError:
            print("\n⚠️ Entrada no válida.\n")

    def eliminar_estudiante(self):
        self.listar_estudiantes()
        if not self.estudiantes:
            return
        try:
            idx = int(input("\nIngrese el número del estudiante a eliminar: ")) - 1
            if 0 <= idx < len(self.estudiantes):
                eliminado = self.estudiantes.pop(idx)
                print(f"\n✅ Estudiante '{eliminado.nombre}' eliminado correctamente.\n")
            else:
                print("\n⚠️ Número inválido.\n")
        except ValueError:
            print("\n⚠️ Entrada no válida.\n")

    ### 🔹 MÉTODOS PARA DOCENTES
    def agregar_docente(self):
        nombre = input("Ingrese el nombre del docente: ")
        edad = int(input("Ingrese la edad del docente: "))
        direccion = input("Ingrese la dirección del docente: ")
        tipoContrato = input("Ingrese el tipo de contrato del docente: ")
        docente = Docente(nombre, edad, direccion, tipoContrato)
        self.docentes.append(docente)
        print("\n✅ Docente agregado correctamente.\n")

    def listar_docentes(self):
        if not self.docentes:
            print("\n⚠️ No hay docentes registrados.\n")
        else:
            print("\n📋 Lista de docentes:")
            for idx, docente in enumerate(self.docentes, start=1):
                print(f"{idx}. {docente}")

    def modificar_docente(self):
        self.listar_docentes()
        if not self.docentes:
            return
        try:
            idx = int(input("\nIngrese el número del docente a modificar: ")) - 1
            if 0 <= idx < len(self.docentes):
                docente = self.docentes[idx]
                docente.nombre = input(f"Nuevo nombre ({docente.nombre}): ") or docente.nombre
                docente.edad = int(input(f"Nueva edad ({docente.edad}): ") or docente.edad)
                docente.direccion = input(f"Nueva dirección ({docente.direccion}): ") or docente.direccion
                docente.tipoContrato = input(f"Nuevo tipo de contrato ({docente.tipoContrato}): ") or docente.tipoContrato
                print("\n✅ Docente modificado correctamente.\n")
            else:
                print("\n⚠️ Número inválido.\n")
        except ValueError:
            print("\n⚠️ Entrada no válida.\n")

    def eliminar_docente(self):
        self.listar_docentes()
        if not self.docentes:
            return
        try:
            idx = int(input("\nIngrese el número del docente a eliminar: ")) - 1
            if 0 <= idx < len(self.docentes):
                eliminado = self.docentes.pop(idx)
                print(f"\n✅ Docente '{eliminado.nombre}' eliminado correctamente.\n")
            else:
                print("\n⚠️ Número inválido.\n")
        except ValueError:
            print("\n⚠️ Entrada no válida.\n")
            
    ### 🔹 MÉTODOS PARA ADMINISTRATIVOS
    def agregar_administrativo(self):
        nombre = input("Ingrese el nombre del administrativo: ")
        edad = int(input("Ingrese la edad del administrativo: "))
        direccion = input("Ingrese la dirección del administrativo: ")
        cargo = input("Ingrese el cargo del administrativo: ")
        administrativo = Administrativo(nombre, edad, direccion, cargo)
        self.administrativo.append(administrativo)
        print("\n✅ Administrativo agregado correctamente.\n")

    def listar_administrativos(self):
        if not self.administrativo:
            print("\n⚠️ No hay administrativos registrados.\n")
        else:
            print("\n📋 Lista de administrativos:")
            for idx, administrativo in enumerate(self.administrativo, start=1):
                print(f"{idx}. {administrativo}")

    def modificar_administrativo(self):
        self.listar_administrativos()
        if not self.administrativo:
            return
        try:
            idx = int(input("\nIngrese el número del administrativo a modificar: ")) - 1
            if 0 <= idx < len(self.administrativo):
                administrativo = self.administrativo[idx]
                administrativo.nombre = input(f"Nuevo nombre ({administrativo.nombre}): ") or administrativo.nombre
                administrativo.edad = int(input(f"Nueva edad ({administrativo.edad}): ") or administrativo.edad)
                administrativo.direccion = input(f"Nueva dirección ({administrativo.direccion}): ") or administrativo.direccion
                administrativo.cargo = input(f"Nuevo cargo ({administrativo.cargo}): ") or administrativo.cargo
                print("\n✅ Administrativo modificado correctamente.\n")
            else:
                print("\n⚠️ Número inválido.\n")
        except ValueError:
            print("\n⚠️ Entrada no válida.\n")

    def eliminar_administrativo(self):
        self.listar_administrativos()
        if not self.administrativo:
            return
        try:
            idx = int(input("\nIngrese el número del administrativo a eliminar: ")) - 1
            if 0 <= idx < len(self.administrativo):
                eliminado = self.administrativo.pop(idx)
                print(f"\n✅ Administrativo '{eliminado.nombre}' eliminado correctamente.\n")
            else:
                print("\n⚠️ Número inválido.\n")
        except ValueError:
            print("\n⚠️ Entrada no válida.\n")

    ### 🔹 MENÚ PRINCIPAL
    def ejecutar(self):
        while True:
            print("\n📚 SISTEMA DE GESTIÓN")
            print("1. Gestión de Estudiantes")
            print("2. Gestión de Docentes")
            print("3. Gestión de Administrativos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_estudiantes()
            elif opcion == "2":
                self.menu_docentes()
            elif opcion == "3":
                self.menu_administrativo()
            elif opcion == "4":
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠️ Opción no válida. Intente de nuevo.\n")

    ### 🔹 SUBMENÚS PARA ESTUDIANTES, DOCENTES Y ADMINISTRATIVOS
    def menu_estudiantes(self):
        while True:
            print("\n🎓 GESTIÓN DE ESTUDIANTES")
            print("1. Agregar estudiante")
            print("2. Listar estudiantes")
            print("3. Modificar estudiante")
            print("4. Eliminar estudiante")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_estudiante()
            elif opcion == "2":
                self.listar_estudiantes()
            elif opcion == "3":
                self.modificar_estudiante()
            elif opcion == "4":
                self.eliminar_estudiante()
            elif opcion == "5":
                break
            else:
                print("\n⚠️ Opción no válida. Intente de nuevo.\n")

    def menu_docentes(self):
        while True:
            print("\n👨‍🏫 GESTIÓN DE DOCENTES")
            print("1. Agregar docente")
            print("2. Listar docentes")
            print("3. Modificar docente")
            print("4. Eliminar docente")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_docente()
            elif opcion == "2":
                self.listar_docentes()
            elif opcion == "3":
                self.modificar_docente()
            elif opcion == "4":
                self.eliminar_docente()
            elif opcion == "5":
                break
            else:
                print("\n⚠️ Opción no válida. Intente de nuevo.\n")
                
    def menu_administrativo(self):
        while True:
            print("\n👨‍🏫 GESTIÓN DE ADMINISTRATIVOS")
            print("1. Agregar administrativo")
            print("2. Listar administrativo")
            print("3. Modificar administrativo")
            print("4. Eliminar administrativo")
            print("5. Volver al menú principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_administrativo()
            elif opcion == "2":
                self.listar_administrativos()
            elif opcion == "3":
                self.modificar_administrativo()
            elif opcion == "4":
                self.eliminar_administrativo()
            elif opcion == "5":
                break
            else:
                print("\n⚠️ Opción no válida. Intente de nuevo.\n")


# Ejecutar el sistema
if __name__ == "__main__":
    sistema = SistemaGestion()
    sistema.ejecutar()