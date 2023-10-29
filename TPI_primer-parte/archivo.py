from datetime import date
fecha_actual = date.today()

class Archivo():

    def __init__(self, nombre, formato):
        self.__nombre = nombre
        self.__fecha_actual = fecha_actual
        self.__formato = formato

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def fecha_actual(self):
        return self.__fecha_actual
    
    @property
    def formato(self):
        return self.__formato
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} \nFecha: {self.__fecha_actual} \nFormato: {self.__formato}"
        
