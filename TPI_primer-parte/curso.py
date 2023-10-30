import random
import string
from archivo import Archivo
from carrera import Carrera

class Curso():
    cursos = []
    __prox_cod = 0

    def __init__(self, carrera, nombre_curso: str = None):
        self.__nombre_curso = nombre_curso
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__codigo = Curso.__prox_cod
        Curso.__prox_cod += 1
        self.archivos = []
        
        if nombre_curso is not None:
            self.nuevo_curso = {'nombre': self.__nombre_curso, 
                                'clave': self.__contrasenia_matriculacion, 
                                'codigo': self.__codigo, 
                                'archivos': self.archivos,
                                'carrera': carrera.nombre}
            Curso.cursos.append(self.nuevo_curso)

    @property
    def nombre_curso(self):
        return self.__nombre_curso
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion
    
    def __str__(self):
        for curso in Curso.cursos:
            print(f"Materia: {curso['nombre']}   Carrera: {curso['carrera']}   Archivos: {curso['archivos']}\n")
        
    def __generar_contrasenia(self) -> str:
        characters = string.ascii_letters + string.digits
        clave = ''.join(random.choice(characters) for i in range(8))
        return clave

    def nuevo_archivo(self, curso_elegido, archivo: Archivo):
        nuevo_archivo = archivo.nombre + "." + archivo.formato
        for curso in Curso.cursos:
            if curso_elegido.nombre_curso == curso['nombre']:
                curso['archivos'].append(nuevo_archivo)
                break
    
