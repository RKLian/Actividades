class MenuPrincipal:
    def __init__(self):
        self.opciones = {
            1: "PERSONAS",
            2: "UNIVERSIDADES",
            3: "NOTAS",
            4: "ASIGNATURA",
            5: "SALIR"
        }
        self.submenus = {
            1: SubmenuPersonas(),
            2: SubmenuUniversidades(),
            3: SubmenuNotas(),
            4: SubmenuAsignaturas()
        }

    def mostrar_menu(self):
        print("MENU PRINCIPAL UNITECNAR")
        for key, value in self.opciones.items():
            print(f"{key}. {value}.")

    def seleccionar_opcion(self, opcion):
        if opcion == 5:
            print("Saliendo del programa...")
            return False
        elif opcion in self.submenus:
            submenu = self.submenus[opcion]
            submenu.mostrar_submenu()
            return True
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            return True


class SubmenuPersonas:
    def __init__(self):
        self.personas = []

    def mostrar_submenu(self):
        while True:
            print("\nSUBMENU PERSONAS")
            opciones_personas = {
                1: "CREAR PERSONA",
                2: "LISTAR PERSONAS",
                3: "ELIMINAR PERSONA",
                4: "ACTUALIZAR",
                5: "ATRAS"
            }
            for key, value in opciones_personas.items():
                print(f"{key}. {value}.")

            opcion = int(input("Seleccione una opción: "))
            if opcion == 5:
                break
            else:
                self.ejecutar_opcion(opcion)

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.crear_persona()
        elif opcion == 2:
            self.listar_personas()
        elif opcion == 3:
            self.eliminar_persona()
        elif opcion == 4:
            self.actualizar_persona()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    def crear_persona(self):
        print("Creando persona...")
        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        identificacion = int(input("Ingrese su identificación: "))
        genero = input("Ingrese el género de la persona: ")
        self.personas.append({"nombre": nombre, "apellido": apellido, "edad": edad, "identificacion": identificacion, "genero": genero})
        print("Persona creada exitosamente.")

    def listar_personas(self):
        print("Listando personas...")
        if self.personas:
            print("Lista de personas:")
            for persona in self.personas:
                print(f"Nombre: {persona['nombre']}, Apellido: {persona['apellido']}, Edad: {persona['edad']}, Identificación: {persona['identificacion']}, Género: {persona['genero']}")
        else:
            print("No hay personas creadas en este momento.")

    def eliminar_persona(self):
        print("Eliminando persona...")
        if self.personas:
            nombre = input("Ingrese el nombre de la persona que desea eliminar: ")
            for persona in self.personas:
                if persona["nombre"] == nombre:
                    self.personas.remove(persona)
                    print("Persona eliminada exitosamente.")
                    return
            print("Persona no encontrada.")
        else:
            print("No hay personas creadas en este momento.")

    def actualizar_persona(self):
        print("Actualizando persona...")
        if self.personas:
            nombre = input("Ingrese el nombre de la persona que desea actualizar: ")
            for persona in self.personas:
                if persona["nombre"] == nombre:
                    nuevo_nombre = input("Ingrese el nuevo nombre de la persona: ")
                    nuevo_apellido = input("Ingrese el nuevo apellido de la persona: ")
                    nueva_edad = int(input("Ingrese la nueva edad de la persona: "))
                    nueva_identificacion = int(input("Ingrese la nueva identificación de la persona: "))
                    nuevo_genero = input("Ingrese el nuevo género de la persona: ")
                    persona["nombre"] = nuevo_nombre
                    persona["apellido"] = nuevo_apellido
                    persona["edad"] = nueva_edad
                    persona["identificacion"] = nueva_identificacion
                    persona["genero"] = nuevo_genero
                    print("Persona actualizada exitosamente.")
                    return
            print("Persona no encontrada.")
        else:
            print("No hay personas creadas en este momento.")


class SubmenuUniversidades:
    def __init__(self):
        self.estudiantes = []

    def mostrar_submenu(self):
        while True:
            print("\nSUBMENU UNIVERSIDADES")
            opciones_universidades = {
                1: "CREAR ESTUDIANTE",
                2: "LISTAR ESTUDIANTE",
                3: "ELIMINAR ESTUDIANTE",
                4: "ACTUALIZAR",
                5: "ATRAS"
            }
            for key, value in opciones_universidades.items():
                print(f"{key}. {value}.")

            opcion = int(input("Seleccione una opción: "))
            if opcion == 5:
                break
            else:
                self.ejecutar_opcion(opcion)

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.crear_estudiante()
        elif opcion == 2:
            self.listar_estudiantes()
        elif opcion == 3:
            self.eliminar_estudiante()
        elif opcion == 4:
            self.actualizar_estudiante()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    def crear_estudiante(self):
        print("Creando estudiante...")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        semestre = int(input("Ingrese el semestre cursado: "))
        jornada = input("Ingrese la jornada: ")
        universidad = input("Ingrese la universidad: ")
        self.estudiantes.append({"nombre": nombre, "apellido": apellido, "semestre": semestre, "jornada": jornada, "universidad": universidad})
        print("Estudiante creado exitosamente.")

    def listar_estudiantes(self):
        print("Listando estudiantes...")
        if self.estudiantes:
            print("Lista de estudiantes:")
            for estudiante in self.estudiantes:
                print(f"Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Semestre: {estudiante['semestre']}, Jornada: {estudiante['jornada']}, Universidad: {estudiante['universidad']}")
        else:
            print("No hay estudiantes creados en este momento.")

    def eliminar_estudiante(self):
        print("Eliminando estudiante...")
        if self.estudiantes:
            nombre = input("Ingrese el nombre del estudiante que desea eliminar: ")
            for estudiante in self.estudiantes:
                if estudiante["nombre"] == nombre:
                    self.estudiantes.remove(estudiante)
                    print("Estudiante eliminado exitosamente.")
                    return
            print("Estudiante no encontrado.")
        else:
            print("No hay estudiantes creados en este momento.")

    def actualizar_estudiante(self):
        print("Actualizando estudiante...")
        if self.estudiantes:
            nombre = input("Ingrese el nombre del estudiante que desea actualizar: ")
            for estudiante in self.estudiantes:
                if estudiante["nombre"] == nombre:
                    nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
                    nuevo_apellido = input("Ingrese el nuevo apellido del estudiante: ")
                    nuevo_semestre = int(input("Ingrese el nuevo semestre cursado: "))
                    nueva_jornada = input("Ingrese la nueva jornada: ")
                    nueva_universidad = input("Ingrese la nueva universidad: ")
                    estudiante["nombre"] = nuevo_nombre
                    estudiante["apellido"] = nuevo_apellido
                    estudiante["semestre"] = nuevo_semestre
                    estudiante["jornada"] = nueva_jornada
                    estudiante["universidad"] = nueva_universidad
                    print("Estudiante actualizado exitosamente.")
                    return
            print("Estudiante no encontrado.")
        else:
            print("No hay estudiantes creados en este momento.")


class SubmenuNotas:
    def __init__(self):
        self.notas = {}

    def mostrar_submenu(self):
        while True:
            print("\nSUBMENU NOTAS")
            opciones_notas = {
                1: "CREAR NOTA",
                2: "LISTAR NOTAS",
                3: "ELIMINAR NOTA",
                4: "ACTUALIZAR",
                5: "ATRAS"
            }
            for key, value in opciones_notas.items():
                print(f"{key}. {value}.")

            opcion = int(input("Seleccione una opción: "))
            if opcion == 5:
                break
            else:
                self.ejecutar_opcion(opcion)

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.crear_nota()
        elif opcion == 2:
            self.listar_notas()
        elif opcion == 3:
            self.eliminar_nota()
        elif opcion == 4:
            self.actualizar_nota()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    def crear_nota(self):
        print("Creando nota...")
        estudiante = input("Ingrese el nombre del estudiante: ")
        nota = float(input("Ingrese la nota del estudiante: "))
        self.notas[estudiante] = nota
        print("Nota creada exitosamente.")

    def listar_notas(self):
        print("Listando notas...")
        if self.notas:
            print("Notas de los estudiantes:")
            for estudiante, nota in self.notas.items():
                print(f"Estudiante: {estudiante}, Nota: {nota}")
        else:
            print("No hay notas establecidas en este momento.")

    def eliminar_nota(self):
        print("Eliminando nota...")
        if self.notas:
            estudiante = input("Ingrese el nombre del estudiante cuya nota desea eliminar: ")
            if estudiante in self.notas:
                del self.notas[estudiante]
                print("Nota eliminada exitosamente.")
            else:
                print("Estudiante no encontrado.")
        else:
            print("No hay notas establecidas en este momento.")

    def actualizar_nota(self):
        print("Actualizando nota...")
        if self.notas:
            estudiante = input("Ingrese el nombre del estudiante cuya nota desea actualizar: ")
            if estudiante in self.notas:
                nueva_nota = float(input("Ingrese la nueva nota del estudiante: "))
                self.notas[estudiante] = nueva_nota
                print("Nota actualizada exitosamente.")
            else:
                print("Estudiante no encontrado.")
        else:
            print("No hay notas establecidas en este momento.")


class SubmenuAsignaturas:
    def __init__(self):
        self.asignaturas = {}

    def mostrar_submenu(self):
        while True:
            print("\nSUBMENU ASIGNATURAS")
            opciones_asignaturas = {
                1: "CREAR ASIGNATURA",
                2: "LISTAR ASIGNATURAS",
                3: "ELIMINAR ASIGNATURA",
                4: "ACTUALIZAR",
                5: "ATRAS"
            }
            for key, value in opciones_asignaturas.items():
                print(f"{key}. {value}.")

            opcion = int(input("Seleccione una opción: "))
            if opcion == 5:
                break
            else:
                self.ejecutar_opcion(opcion)

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.crear_asignatura()
        elif opcion == 2:
            self.listar_asignaturas()
        elif opcion == 3:
            self.eliminar_asignatura()
        elif opcion == 4:
            self.actualizar_asignatura()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    def crear_asignatura(self):
        print("Creando asignatura...")
        codigo = input("Ingrese el código de la asignatura: ")
        nombre = input("Ingrese el nombre de la asignatura: ")
        self.asignaturas[codigo] = nombre
        print("Asignatura creada exitosamente.")

    def listar_asignaturas(self):
        print("Listando asignaturas...")
        if self.asignaturas:
            print("Asignaturas:")
            for codigo, nombre in self.asignaturas.items():
                print(f"Código: {codigo}, Nombre: {nombre}")
        else:
            print("No hay asignaturas disponibles en este momento.")

    def eliminar_asignatura(self):
        print("Eliminando asignatura...")
        if self.asignaturas:
            codigo = input("Ingrese el código de la asignatura que desea eliminar: ")
            if codigo in self.asignaturas:
                del self.asignaturas[codigo]
                print("Asignatura eliminada exitosamente.")
            else:
                print("Asignatura no encontrada.")
        else:
            print("No hay asignaturas disponibles en este momento.")

    def actualizar_asignatura(self):
        print("Actualizando asignatura...")
        if self.asignaturas:
            codigo = input("Ingrese el código de la asignatura que desea actualizar: ")
            if codigo in self.asignaturas:
                nuevo_nombre = input("Ingrese el nuevo nombre de la asignatura: ")
                self.asignaturas[codigo] = nuevo_nombre
                print("Asignatura actualizada exitosamente.")
            else:
                print("Asignatura no encontrada.")
        else:
            print("No hay asignaturas disponibles en este momento.")
