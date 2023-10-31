from curso import Curso
from estudiante import Estudiante
from profesor import Profesor
from archivo import Archivo
from carrera import Carrera

def submenu_alumno():
    rta_eleccion = ''
    print("Ha ingresado como alumno.")
    print("Ingrese los siguientes datos: ")
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    email = str(input("Email: "))
    contrasenia = str(input("Contraseña: "))
    legajo = int(input("Legajo: "))
    anio_insc_carrera = int(input("Año de inscripción a la carrera: "))
    print()

    estudiante = Estudiante(nombre, apellido, email, contrasenia, legajo, anio_insc_carrera)
    if estudiante.validar_credenciales(email, contrasenia):
        print("Email y contraseña son correctos. \n")
        while rta_eleccion != 'salir':
            print("Sub menú alumno:")
            print("1. Matricularse a un curso")
            print("2. Desmatricularse a un curso")
            print("3. Ver cursos matriculados")
            print("4. Volver al menú principal")
            opcion = input("Ingrese una opción: ")
            print()

            if opcion == "1":
                curso = Curso(carrera)
                estudiante.matricular_en_curso(curso)
                print()
            elif opcion == "2":
                estudiante.desmatricularse_de_curso(curso)
            elif opcion == "3":
                estudiante.mostrar_cursos_matriculados(curso)
                print()
            elif opcion == "4":
                rta_eleccion = 'salir'
            else:
                print("Opción inválida. \n")
    else:
        print("Contraseña incorrecta o estudiante inexistente. Debe registrarse en alumnado. \n")


def submenu_profesor():
    rta_eleccion = ''
    print("Ha ingresado como profesor.")
    print("Ingrese los siguientes datos: ")
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    email = str(input("Email: "))
    contrasenia = str(input("Contraseña: "))
    titulo = str(input("Título: "))
    anio_egreso = int(input("Año de egreso: "))
    print()

    profesor = Profesor(nombre, apellido, email, contrasenia, titulo, anio_egreso)
    if profesor.validar_credenciales(email, contrasenia):
        print("Email y contraseña son correctos. \n")
        while rta_eleccion != 'salir':
            print("Sub menú profesor:")
            print("1. Dictar curso")
            print("2. Ver curso")
            print("3. Volver al menú principal")
            eleccion = int(input("Elija una opción: "))
            print()

            if eleccion == 1:
                nombre_curso = str(input("Ingrese el nombre del curso: "))
                curso = Curso(carrera, nombre_curso)
                profesor.dictar_curso(curso)
            elif eleccion == 2:
                if profesor.mis_cursos == []:
                    print("Aún no hay cursos dados de alta. \n")
                else:
                    profesor.mostrar_cursos()
                    curso_elegido = int(input("Seleccione un curso: "))
                    print()
                    if 1 <= curso_elegido <= len(profesor.mis_cursos):
                        curso_elegido = profesor.mis_cursos[curso_elegido - 1]
                        print(f"Nombre: {curso_elegido.nombre_curso}")
                        print(f"Código: {curso_elegido.codigo}")
                        print(f"Contraseña: {curso_elegido.contrasenia_matriculacion}")
                        print(f"Cantidad de archivos: {len(curso_elegido.archivos)} \n")
                        
                        print("Desea agregar un archivo adjunto? \n1. Sí \n2. No")
                        op_elegida = int(input("Seleccione una opción: "))
                        if op_elegida == 1:
                            nombre = str(input("Nombre del archivo: "))
                            formato = str(input("Formato: "))
                            archivo = Archivo(nombre, formato)
                            curso.nuevo_archivo(curso_elegido, archivo)
                        elif op_elegida == 2:
                            print()
                        else:
                            print("Opción inválida. \n")
                    else:
                        print("Opción no válida. Por favor, ingrese un número de curso válido. \n")
            elif eleccion == 3:
                rta_eleccion = 'salir'  
            else:
                print("Ingrese una opción válida.\n")
    else:
        print("Contraseña incorrecta o profesor inexistente. Debe registrarse en alumnado. \n")


carrera = Carrera('Tecnicatura Universitaria en Programación', 2)
curso = Curso(carrera)
rta = ''
while rta != 'salir':
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
    opt = int(input("Seleccione una opción: "))
    print()

    if opt == 1:
        submenu_alumno() 
    elif opt == 2:
        submenu_profesor()
    elif opt == 3:
        if curso.cursos == []:
            print("No hay cursos disponibles.")
            print()
        else: 
            curso.__str__()
    elif opt == 4:
        rta = 'salir'
    else:
        print("Ingrese una opción válida.\n")

print("Fin del programa. Gracias!")