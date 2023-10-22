"""from abc import ABC, abstractmethod
import random
import string

class Usuario(ABC):
    def __init__(self, nombre:str, apellido:str, email:str, contrasenia:str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def contrasenia(self):
        return self.__contrasenia

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def validar_credenciales(self, email:str, contrasenia:str):
        pass
    
class Estudiante(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int = None, anio_insc_carrera: int = None):
        super().__init__(nombre, apellido, email, contrasenia)

        self.alumnos = []
        self.alumn1 = {'email': 'pepe@gmail.com', 'contrasenia': 'pepe123'}
        self.alumn2 = {'email': 'paula@gmail.com', 'contrasenia': 'paula123'}
        self.alumnos.append(self.alumn1)
        self.alumnos.append(self.alumn2)
        self.__legajo = legajo
        self.__anio_insc_carrera = anio_insc_carrera

        self.curso = None
        self.mis_cursos = []

    @property
    def legajo(self):
        return self.__legajo
    
    @property
    def anio_insc_carrera(self):
        return self.__anio_insc_carrera

    def __str__(self):
        return super().__str__()
    
    def validar_credenciales(self, email: str, contrasenia: str):
        super().validar_credenciales(email, contrasenia)
        self.email_encontrado = False
        
        for alumno in self.alumnos:
            if email == alumno['email']:
                self.email_encontrado = True
                break

        if self.email_encontrado:
            if contrasenia == alumno['contrasenia']:
                return True
            else:
                return False
        else:
            print("No se encontró un alumno con ese email. Debe registrarse en alumnado.")
        
    
    def matricular_en_curso(self, curso):
        self.curso = curso
        self.mis_cursos.append(self.curso)
        return f"Cursos: {self.mis_cursos}"

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str = None, anio_egreso: int = None):
        super().__init__(nombre, apellido, email, contrasenia)

        self.profesores = []
        self.prof1 = {'email': 'juan@gmail.com', 'contrasenia': 'juan123'}
        self.prof2 = {'email': 'alberto@gmail.com', 'contrasenia': 'alberto123'}
        self.profesores.append(self.prof1)
        self.profesores.append(self.prof2)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.mis_cursos = [] 
        self.email_encontrado = False

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso

    def __str__(self):
        return super().__str__()
    
    def dictar_curso(self):
        pass

    def validar_credenciales(self, email: str, contrasenia: str):
        super().validar_credenciales(email, contrasenia)
        self.email_encontrado = False

        for profe in self.profesores:
            if email == profe['email']:
                self.email_encontrado = True
                break

        if self.email_encontrado:
            if contrasenia == profe['contrasenia']:
                return True
            else:
                return False
        else:
            return f"No se encontró un alumno con ese email. Debe registrarse en alumnado."
        

class Curso():
    carrera = 'Tecnicatura Universitaria en Programación'
    cursos = []
    curso1 = {'nombre': 'Inglés I', 'clave': 'ingles123'}
    curso2 = {'nombre': 'Inglés II', 'clave': 'ingles2_123'}
    curso3 = {'nombre': 'Laboratorio I', 'clave': 'lab123'}
    curso4 = {'nombre': 'Laboratorio II', 'clave': 'lab2_123'}
    curso5 = {'nombre': 'Programación I', 'clave': 'prog123'}
    curso6 = {'nombre': 'Programación II', 'clave': 'prog2_123'}
    cursos.append(curso1)
    cursos.append(curso2)
    cursos.append(curso3)
    cursos.append(curso4)
    cursos.append(curso5)
    cursos.append(curso6)
    
    def __init__(self, nombre_curso:str = None, contrasenia_matriculacion:str = None):
        self.__nombre_curso = nombre_curso
        self.__contrasenia_matriculacion = contrasenia_matriculacion
        self.mi_cursos = []

    @property
    def nombre_curso(self):
        return self.__nombre_curso
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    def __str__(self):
        for curso in self.cursos:
            print(f"Materia: {curso['nombre']}   Carrera: {self.carrera}")
    
    def __generar_contrasenia(self) -> str:
        characters = string.ascii_letters + string.digits
        clave = ''.join(random.choice(characters) for i in range(8))
        return clave

    def matricularse(self):
        self.mostrar_cursos()
        opcion = input("Ingrese el número del curso al que desea matricularse: ")
        if opcion.isdigit():
            codigo_curso = int(opcion)
            if codigo_curso >= 1 and codigo_curso <= len(self.cursos):
                curso_seleccionado = self.cursos[codigo_curso - 1]
                nombre_curso = curso_seleccionado['nombre']
                contraseña_correcta = curso_seleccionado['clave']
                if nombre_curso not in self.mi_cursos:
                    contraseña = input("Ingrese la contraseña de matriculación: ")
                    if contraseña == contraseña_correcta:
                        self.mi_cursos.append(nombre_curso)
                        print("Matriculación exitosa")
                    else:
                        print("Contraseña incorrecta. Matriculación fallida.")
                else:
                    print("Ya estás matriculado en ese curso.")
            else:
                print("Opción inválida.")
        else:
            print("Opción inválida.")

    def mostrar_cursos(self):
        print("Cursos disponibles:")
        for i, curso in enumerate(self.cursos, 1):
            print(f"{i}. {curso['nombre']}")
    
    def mostrar_cursos_matriculados(self):
        print("Cursos matriculados:")
        if len(self.mi_cursos) > 0:
            for curso in self.mi_cursos:
                print(curso)
            opcion = int(input("Ingrese el número del curso que desea ver: ")) #completar
        else:
            print("No estás matriculado en ningún curso.")
    
    def submenu_alumno(self):
        while True:
            print("Sub menú alumno:")
            print("1. Matricularse a un curso")
            print("2. Ver cursos matriculados")
            print("3. Volver al menú principal")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.matricularse()
            elif opcion == "2":
                self.mostrar_cursos_matriculados()
            elif opcion == "3":
                self.ver_archivos_curso()
                break
            else:
                print("Opción inválida.")

rta = ''
while rta!='salir':
    print("Seleccione una opción:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    opt = int(input())

    if opt == 1:
        print("Ingrese los siguientes datos: ")
        nombre = str(input("Nombre: "))
        apellido = str(input("Apellido: "))
        email = str(input("Email: "))
        contrasenia = str(input("Contraseña: "))

        persona1 = Estudiante(nombre, apellido, email, contrasenia)
        if persona1.validar_credenciales(email, contrasenia):
            print("Email y contraseña son correctos.")
            print("MENU")
            print("MENU")
            print("MENU")
            curso = Curso()
            curso.submenu_alumno()
        else:
            print("La contraseña no coincide con el email ingresado.")
    elif opt == 2:
        print("Ingrese los siguientes datos: ")
        nombre = str(input("Nombre: "))
        apellido = str(input("Apellido: "))
        email = str(input("Email: "))
        contrasenia = str(input("Contraseña: "))

        persona1 = Profesor(nombre, apellido, email, contrasenia)
        persona1.validar_credenciales(email, contrasenia)
    elif opt == 3:
        cursos = Curso()
        cursos.__str__()
    elif opt == 4:
        rta = 'salir'
    else:
        print("Ingrese una opción válida. \n")

print("Fin del programa. Gracias!")"""


from abc import ABC, abstractmethod
import random
import string

class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def email(self):
        return self.__email
    
    @property
    def contrasenia(self):
        return self.__contrasenia

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def validar_credenciales(self, email: str, contrasenia: str):
        pass

class Curso():
    cursos = [
        {'nombre': 'Inglés I', 'clave': 'ingles123'},
        {'nombre': 'Inglés II', 'clave': 'ingles2_123'},
        {'nombre': 'Laboratorio I', 'clave': 'lab123'},
        {'nombre': 'Laboratorio II', 'clave': 'lab2_123'},
        {'nombre': 'Programación I', 'clave': 'prog123'},
        {'nombre': 'Programación II', 'clave': 'prog2_123'}
        ]
    
    def __init__(self, nombre_curso: str = None):
        self.__nombre_curso = nombre_curso
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.carrera = 'Tecnicatura Universitaria en Programación'
        
        if nombre_curso is not None:
            self.nuevo_curso = {'nombre': self.__nombre_curso, 'clave': self.__contrasenia_matriculacion}
            self.cursos.append(self.nuevo_curso)

    @property
    def nombre_curso(self):
        return self.__nombre_curso
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    def __str__(self):
        result = ""
        for curso in self.cursos:
            result += f"Materia: {curso['nombre']}   Carrera: {self.carrera}\n"
        return result

    def __generar_contrasenia(self) -> str:
        characters = string.ascii_letters + string.digits
        clave = ''.join(random.choice(characters) for i in range(8))
        return clave

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int = None, anio_insc_carrera: int = None):
        super().__init__(nombre, apellido, email, contrasenia)
        self.alumnos = []
        self.alumn1 = {'email': 'pepe@gmail.com', 'contrasenia': 'pepe123'}
        self.alumn2 = {'email': 'paula@gmail.com', 'contrasenia': 'paula123'}
        self.alumnos.append(self.alumn1)
        self.alumnos.append(self.alumn2)
        self.__legajo = legajo
        self.__anio_insc_carrera = anio_insc_carrera
        self.mi_cursos = []

    @property
    def legajo(self):
        return self.__legajo
    
    @property
    def anio_insc_carrera(self):
        return self.__anio_insc_carrera

    def __str__(self):
        return super().__str__()
    
    def validar_credenciales(self, email: str, contrasenia: str):
        super().validar_credenciales(email, contrasenia)
        self.email_encontrado = False
        
        for alumno in self.alumnos:
            if email == alumno['email']:
                self.email_encontrado = True
                break

        if self.email_encontrado:
            if contrasenia == alumno['contrasenia']:
                return True
            else:
                return False
        else:
            print("No se encontró un alumno con ese email. Debe registrarse en alumnado.")
            return False
    
    def matricular_en_curso(self, curso: Curso):
        print("Cursos disponibles:")
        for i, cur in enumerate(curso.cursos, 1):
            print(f"{i}. {cur['nombre']}")

        opcion = input("Ingrese el número del curso al que desea matricularse: ")
        if opcion.isdigit():
            codigo_curso = int(opcion)
            if codigo_curso >= 1 and codigo_curso <= len(curso.cursos):
                curso_seleccionado = curso.cursos[codigo_curso - 1]
                nombre_curso = curso_seleccionado['nombre']
                contraseña_correcta = curso_seleccionado['clave']
                if nombre_curso not in self.mi_cursos:
                    contraseña = input("Ingrese la contraseña de matriculación: ")
                    if contraseña == contraseña_correcta:
                        self.mi_cursos.append(nombre_curso)
                        print("Matriculación exitosa")
                    else:
                        print("Contraseña incorrecta. Matriculación fallida.")
                else:
                    print("Ya estás matriculado en ese curso.")
            else:
                print("Opción inválida.")
        else:
            print("Opción inválida.")

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str = None, anio_egreso: int = None):
        super().__init__(nombre, apellido, email, contrasenia)
        self.profesores = [
            {'email': 'juan@gmail.com', 'contrasenia': 'juan123'},
            {'email': 'alberto@gmail.com', 'contrasenia': 'alberto123'}
        ]
        self.mis_cursos = []
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.email_encontrado = False

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso

    def __str__(self):
        super().__str__()
        for i in range(len(self.mis_cursos)):
            print(f"{i + 1}. {self.mis_cursos[i].nombre_curso}")
    
    def dictar_curso(self, curso: Curso):
        self.mis_cursos.append(curso)
        print("Curso agregado exitosamente.")
        print(f"Nombre: {curso.nombre_curso} \nContraseña {curso.contrasenia_matriculacion}")

    def validar_credenciales(self, email: str, contrasenia: str):
        super().validar_credenciales(email, contrasenia)
        self.email_encontrado = False

        for profe in self.profesores:
            if email == profe['email']:
                self.email_encontrado = True
                break

        if self.email_encontrado:
            if contrasenia == profe['contrasenia']:
                return True
            else:
                return False
        else:
            print("No se encontró un profesor con ese email. Debe registrarse como profesor.")
            return False


def submenu_alumno():
    rta_eleccion = ''
    print("Ha ingresado como alumno.")
    print("Ingrese los siguientes datos: ")
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    email = str(input("Email: "))
    contrasenia = str(input("Contraseña: "))
    print()

    estudiante = Estudiante(nombre, apellido, email, contrasenia)
    if estudiante.validar_credenciales(email, contrasenia):
        print("Email y contraseña son correctos.")
        while rta_eleccion != 'salir':
            print("Sub menú alumno:")
            print("1. Matricularse a un curso")
            print("2. Ver cursos matriculados")
            print("3. Volver al menú principal")
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                curso = Curso()
                estudiante.matricular_en_curso(curso)
            elif opcion == "2":
                print("Cursos matriculados:")
                if len(estudiante.mi_cursos) > 0:
                    for curso in estudiante.mi_cursos:
                        print(curso)
                    #opcion = int(input("Ingrese el número del curso que desea ver: ")) #completar
                else:
                    print("No estás matriculado en ningún curso.")
            elif opcion == "3":
                rta_eleccion = 'salir'
            else:
                print("Opción inválida.")
    else:
        print("La contraseña no coincide con el email ingresado.")


def submenu_profesor():
    rta_eleccion = ''
    print("Ha ingresado como profesor.")
    print("Ingrese los siguientes datos: ")
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    email = str(input("Email: "))
    contrasenia = str(input("Contraseña: "))
    print()

    profesor = Profesor(nombre, apellido, email, contrasenia)
    if profesor.validar_credenciales(email, contrasenia):
        print("Email y contraseña son correctos.")
        while rta_eleccion != 'salir':
            print("Elija una opción:")
            print("1. Dictar curso")
            print("2. Ver curso")
            print("3. Volver al menú principal")
            eleccion = int(input())
            print()

            if eleccion == 1:
                nombre_curso = str(input("Ingrese el nombre del curso: "))
                curso = Curso(nombre_curso)
                profesor.dictar_curso(curso)
            elif eleccion == 2:
                if profesor.mis_cursos == []:
                    print("Aún no hay cursos dados de alta.")
                else:
                    profesor.__str__()
                    curso_elegido = int(input("Seleccione un curso: \n"))
                    if 1 <= curso_elegido <= len(profesor.mis_cursos):
                        curso_elegido = profesor.mis_cursos[curso_elegido - 1]
                        print(f"Nombre: {curso_elegido.nombre_curso}")
                        print(f"Contraseña: {curso_elegido.contrasenia_matriculacion} \n")
                    else:
                        print("Opción no válida. Por favor, ingrese un número de curso válido. \n")
            elif eleccion == 3:
                rta_eleccion = 'salir'  
            else:
                print("Ingrese una opción válida.\n")
    else:
        print("La contraseña no coincide con el email ingresado.")


curso = Curso()
rta = ''
while rta != 'salir':
    print("Seleccione una opción:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    opt = int(input())
    print()

    if opt == 1:
        submenu_alumno()
    elif opt == 2:
        submenu_profesor()
    elif opt == 3:
        print(curso)  
    elif opt == 4:
        rta = 'salir'
    else:
        print("Ingrese una opción válida.\n")

print("Fin del programa. Gracias!")
