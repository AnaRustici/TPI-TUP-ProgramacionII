from curso import Curso
from estudiante import Estudiante
from profesor import Profesor

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
            print("2. Ver cursos matriculados")
            print("3. Volver al menú principal")
            opcion = input("Ingrese una opción: ")
            print()

            if opcion == "1":
                curso = Curso()
                estudiante.matricular_en_curso(curso)
                print()
            elif opcion == "2":
                estudiante.mostrar_cursos_matriculados()
                print()
            elif opcion == "3":
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
                curso = Curso(nombre_curso)
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
                        print(f"Contraseña: {curso_elegido.contrasenia_matriculacion} \n")
                    else:
                        print("Opción no válida. Por favor, ingrese un número de curso válido. \n")
            elif eleccion == 3:
                rta_eleccion = 'salir'  
            else:
                print("Ingrese una opción válida.\n")
    else:
        print("Contraseña incorrecta o profesor inexistente. Debe registrarse en alumnado. \n")


curso = Curso()
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
            print(curso)  
    elif opt == 4:
        rta = 'salir'
    else:
        print("Ingrese una opción válida.\n")

print("Fin del programa. Gracias!")