import random
import string
from archivo import Archivo

class Curso():
    cursos = []
    __prox_cod = -1

    def __init__(self, carrera, nombre_curso: str = None):
        self.__nombre_curso = nombre_curso
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__codigo = Curso.generar_codigo()
        self.archivos = []

        #Agregamos los datos del curso y después lo agregamos a la lista de cursos
        if nombre_curso is not None:
            self.nuevo_curso = {
                'nombre': self.__nombre_curso, 
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
    
    @classmethod
    def generar_codigo(cls):
        cls.__prox_cod += 1
        return cls.__prox_cod
    
    def __str__(self):
        #Ordenamos los cursos alfabéticamente
        cursos_ordenados = sorted(Curso.cursos, key=lambda n: n['nombre'])
        for curso in cursos_ordenados:
            print(f"Materia: {curso['nombre']}   Carrera: {curso['carrera']}")
        
    def __generar_contrasenia(self) -> str:
        characters = string.ascii_letters + string.digits
        clave = ''.join(random.choice(characters) for i in range(8))
        return clave

    def nuevo_archivo(self, curso_elegido, archivo: Archivo):
        #Concatenamos el nombre y el formato del curso
        nuevo_archivo = archivo.nombre + "." + archivo.formato
        for curso in Curso.cursos:
            #Validamos que el curso elegido(de la lista del profesor) sea el mismo que se encuentra en la lista de cursos y agregamos el nuevo archivo
            if curso_elegido.nombre_curso == curso['nombre']:
                curso['archivos'].append(nuevo_archivo)
                break
    
    
