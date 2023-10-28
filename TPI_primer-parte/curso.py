import random
import string

class Curso():
    cursos = []
    carrera = 'Tecnicatura Universitaria en Programación'

    def __init__(self, nombre_curso: str = None):
        self.__nombre_curso = nombre_curso
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        
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
        resultado = ""
        for curso in self.cursos:
            resultado += f"Materia: {curso['nombre']}   Carrera: {self.carrera}\n"
            return resultado
        

    def __generar_contrasenia(self) -> str:
        characters = string.ascii_letters + string.digits
        clave = ''.join(random.choice(characters) for i in range(8))
        return clave