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
        #Primero buscamos el email en la lista de profesores
        for alumno in Estudiante.alumnos:
            if email == alumno['email']:
                self.email_encontrado = True
                break

        if self.email_encontrado:
            #Si se encuentra el email, validamos la contraseña
            if contrasenia == alumno['contrasenia']:
                return True
            else:
                return False
        else:
            return False
    
    def matricular_en_curso(self, curso: Curso):
        cursos_disponibles = False
        #Validamos que haya cursos disponibles. Si los hay, se muestran
        if curso.cursos == []:
            cursos_disponibles = False
        else:
            cursos_disponibles = True
            print("Cursos disponibles:")
            for i, cur in enumerate(curso.cursos, 1):
                print(f"{i}. {cur['nombre']}")
        
        print()

        if cursos_disponibles:
            opcion = input("Ingrese el número del curso al que desea matricularse: ")
            print()
            #Validamos que la opción elegida sea un número
            if opcion.isdigit():
                #Asignamos la opción a una nueva variable para hacer las validaciones correspondientes
                opcion_curso = int(opcion)
                if opcion_curso >= 1 and opcion_curso <= len(curso.cursos):
                    #Asignamos el curso que se eligió a una nueva variable, restándole 1, ya que cuando se muestran los cursos el índice arranca en 1
                    curso_seleccionado = curso.cursos[opcion_curso - 1]
                    nombre_curso = curso_seleccionado['nombre']
                    contraseña_correcta = curso_seleccionado['clave']
                    curso_matric = {'nombre': nombre_curso, 'clave': contraseña_correcta}
                    #Validamos que el curso no esté ya en la lista de cursos del alumno
                    if curso_matric not in self.mi_cursos:
                        contraseña = input("Ingrese la contraseña de matriculación: ")
                        print()
                        #Validamos que la contraseña del curso sea la correcta y lo agregamos a la lista de cursos del alumno
                        if contraseña == contraseña_correcta:
                            self.mi_cursos.append(curso_matric)
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
                print(f"{i}. {curso['nombre']}")
            print()
            # Solicita al usuario el número del curso que desea ver
            opcion_curso = input("Ingrese el número del curso que desea ver: ")
            print()
            if opcion_curso.isdigit():
                codigo_curso = int(opcion_curso)
                # Verifica si el número del curso seleccionado es válido
                if codigo_curso >= 1 and codigo_curso <= len(self.mi_cursos):
                    curso_select = codigo_curso - 1
                     # Busca el curso seleccionado en la lista de cursos
                    for curso in Curso.cursos:
                        if self.mi_cursos[curso_select]['nombre'] == curso['nombre']:
                            # Verifica si el curso tiene archivos asociados 
                            if len(curso['archivos']) > 0:
                                print(curso['nombre'])
                                for arch in curso['archivos']:
                                    print(arch)
                                print()
                            else:
                                print("No hay archivos disponibles para este curso.")
                                print()
                            break
                else:
                    print("Opción inválida.")
            else:
                print("Opción inválida.")
        else:
            print("No estás matriculado en ningún curso.")

    def desmatricularse_de_curso(self, curso: Curso):
        if not self.mi_cursos:  # Verifica si no hay cursos matriculados
            print("No estás matriculado en ningún curso.")
            return

        print("Cursos en los que estás matriculado:")
        for i, curso in enumerate(self.mi_cursos, 1):
            print(f"{i}. {curso['nombre']}")
        # Solicita al usuario el número del curso del que desea desmatricularse
        opcion = input("Ingrese el número del curso del que desea desmatricularse: ")
        print()

        if opcion.isdigit() and 1 <= int(opcion) <= len(self.mi_cursos):
            curso_desmatricular = self.mi_cursos[int(opcion) - 1]
            self.mi_cursos.remove(curso_desmatricular)
            # Elimina el curso seleccionado de la lista de cursos matriculados
            print(f"Te has desmatriculado del curso: {curso_desmatricular['nombre']}")
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
    
    