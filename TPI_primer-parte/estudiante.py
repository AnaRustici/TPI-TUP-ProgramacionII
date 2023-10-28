from usuario import Usuario
from curso import Curso

class Estudiante(Usuario):
    alumnos = [
        {'email': 'pepe@gmail.com', 'contrasenia': 'pepe123'},
        {'email': 'paula@gmail.com', 'contrasenia': 'paula123'}
    ]
    
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_insc_carrera: int):
        super().__init__(nombre, apellido, email, contrasenia)
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
        super().__str__()
        return f"Nombre: {self.__nombre} \nApellido: {self.__apellido} \nEmail: {self.__email} \nLegajo: {self.__legajo}"
    
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
            return False
    
    def matricular_en_curso(self, curso: Curso):
        self.cursos_disponibles = False

        if curso.cursos == []:
            self.cursos_disponibles = False
        else:
            self.cursos_disponibles = True
            print("Cursos disponibles:")
            for i, cur in enumerate(curso.cursos, 1):
                print(f"{i}. {cur['nombre']}")
        
        print()

        if self.cursos_disponibles:
            opcion = input("Ingrese el número del curso al que desea matricularse: ")
            print()
            if opcion.isdigit():
                codigo_curso = int(opcion)
                if codigo_curso >= 1 and codigo_curso <= len(curso.cursos):
                    curso_seleccionado = curso.cursos[codigo_curso - 1]
                    nombre_curso = curso_seleccionado['nombre']
                    contraseña_correcta = curso_seleccionado['clave']
                    if nombre_curso not in self.mi_cursos:
                        contraseña = input("Ingrese la contraseña de matriculación: ")
                        print()
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
        else:
            print("No hay cursos disponibles.")
    
    def mostrar_cursos_matriculados(self):
        if len(self.mi_cursos) > 0:
            print("Cursos matriculados:")
            for i, curso in enumerate(self.mi_cursos, 1):
                print(f"{i}. {curso}")
            print()

            opcion_curso = input("Ingrese el número del curso que desea ver: ")
            print()
            if opcion_curso.isdigit():
                codigo_curso = int(opcion_curso)
                if codigo_curso >= 1 and codigo_curso <= len(self.mi_cursos):
                    print("Todavía no se encuentran disponibles los archivos.")
                else:
                    print("Opción inválida.")
            else:
                print("Opción inválida.")
        else:
          print("No estás matriculado en ningún curso.")