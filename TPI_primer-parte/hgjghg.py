from abc import ABC, abstractmethod
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

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str = None, anio_egreso: int = None):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.mis_cursos = []  # Inicializar mis_cursos como una lista vacía específica para cada profesor
        self.email_encontrado = False  # Inicializar email_encontrado
        self.profesores = []
        self.prof1 = {'email': 'juan@gmail.com', 'contrasenia': 'juan123'}
        self.prof2 = {'email': 'alberto@gmail.com', 'contrasenia': 'alberto123'}
        self.profesores.append(self.prof1)
        self.profesores.append(self.prof2)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def anio_egreso(self):
        return self.__anio_egreso
    
    def __str__(self):
        return super().__str__()

    def validar_credenciales(self, email: str, contrasenia: str):
        # Llama al método de la clase base para validar las credenciales
        if not super().validar_credenciales(email, contrasenia):
            return False

        # Agrega la lógica adicional para validar el profesor específico
        if email == self.email and contrasenia == self.contrasenia:
            return True
        else:
            return False


print("Ingrese los siguientes datos: ")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
email = input("Email: ")
contrasenia = input("Contraseña: ")

persona1 = Profesor(nombre, apellido, email, contrasenia)

# Validar credenciales
persona1.validar_credenciales(email, contrasenia)
if persona1.email_encontrado:
    print("Email encontrado en la lista de profesores.")
    # Lógica para comparar la contraseña ingresada con la contraseña del profesor
    # Debes implementar la lógica para manejar 'profe' adecuadamente
else:
    print("No se encontró un profesor con ese email. Debe registrarse como profesor.")
