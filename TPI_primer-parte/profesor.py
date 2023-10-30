from usuario import Usuario
from curso import Curso
from archivo import Archivo

class Profesor(Usuario):
    profesores = [
        {'email': 'juan@gmail.com', 'contrasenia': 'juan123'},
        {'email': 'alberto@gmail.com', 'contrasenia': 'alberto123'}
    ]

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str = None, anio_egreso: int = None):
        super().__init__(nombre, apellido, email, contrasenia)
        self.mis_cursos = []
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso

    def __str__(self):
        super().__str__()
        return f"Nombre: {self.__nombre} \nApellido: {self.__apellido} \nEmail: {self.__email} \nLegajo: {self.__titulo}"
    
    def dictar_curso(self, curso: Curso):
        self.mis_cursos.append(curso)
        print("Curso agregado exitosamente. \n")
        print(f"Nombre: {curso.nombre_curso} \nCódigo: {curso.codigo}\nContraseña {curso.contrasenia_matriculacion}")
        print()

    def mostrar_cursos(self):
        for i in range(len(self.mis_cursos)):
            print(f"{i + 1}. {self.mis_cursos[i].nombre_curso}")

    def validar_credenciales(self, email: str, contrasenia: str):
        super().validar_credenciales(email, contrasenia)
        self.email_encontrado = False

        for profe in Profesor.profesores:
            if email == profe['email']:
                self.email_encontrado = True
                break

        if self.email_encontrado:
            if contrasenia == profe['contrasenia']:
                return True
            else:
                return False
        else:
            return False