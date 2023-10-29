class Carrera():
    def __init__(self, nombre, cant_anios):
        self.__nombre = nombre
        self.__cant_anios = cant_anios

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def cant_anios(self):
        return self.__cant_anios
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} \nCantidad de años: {self.__cant_anios}"
    
    def get_cantidad_materias(self):
        pass