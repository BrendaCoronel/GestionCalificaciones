import json

# Cargar datos de usuarios y roles desde el archivo JSON
def cargar_datos():
    try:
        with open('usuarios.json', 'r') as file:
            data = json.load(file)
            return data['usuarios']
    except FileNotFoundError:
        return []

# Verificar credenciales y autenticar al usuario
def autenticar_usuario(nombre_usuario, contrasena):
    usuarios = cargar_datos()
    for usuario in usuarios:
        if usuario['nombre_usuario'] == nombre_usuario and usuario['contrasena'] == contrasena:
            return usuario['rol']
    return None

# Función para mostrar el perfil del usuario
def mostrar_perfil(rol):
    if rol == 'admin':
        print("Bienvenido, Administrador")
        # Aquí puedes implementar la lógica para la administración de roles y configuraciones.
    elif rol == 'alumno':
        print("Bienvenido, Alumno")
        # Aquí puedes implementar la lógica para mostrar calificaciones y datos personales.
    elif rol == 'profesor':
        print("Bienvenido, Profesor")
        # Aquí puedes implementar la lógica para cargar y modificar notas.

# Función para que un alumno pueda ver sus calificaciones
def ver_calificaciones_alumno(usuarios, nombre_usuario):
    for usuario in usuarios:
        if usuario['nombre_usuario'] == nombre_usuario and usuario['rol'] == 'alumno':
            if 'calificaciones' in usuario:
                print(f"Calificaciones para {nombre_usuario}:")
                for calificacion in usuario['calificaciones']:
                    print(f"Asignatura: {calificacion['asignatura']}, Calificación: {calificacion['calificacion']}")
                return

    print("No se encontró al alumno o no tiene calificaciones registradas.")

# Función para registrar una calificación para un alumno
def registrar_calificacion(usuarios, nombre_usuario):
    alumno = input("Ingrese el nombre del alumno: ")
    asignatura = input("Ingrese la asignatura: ")
    calificacion = input("Ingrese la calificación: ")

    for usuario in usuarios:
        if usuario['nombre_usuario'] == nombre_usuario and usuario['rol'] == 'profesor':
            if 'calificaciones' not in usuario:
                usuario['calificaciones'] = []

            usuario['calificaciones'].append({
                'alumno': alumno,
                'asignatura': asignatura,
                'calificacion': calificacion
            })

            with open('usuarios.json', 'w') as file:
                json.dump({'usuarios': usuarios}, file, indent=4)
            print("Calificación registrada con éxito.")
            return

    print("No se encontró al profesor.")

# Función para consultar y modificar calificaciones
def consultar_y_modificar_calificaciones(usuarios, nombre_usuario):
    alumno = input("Ingrese el nombre del alumno: ")
    asignatura = input("Ingrese la asignatura: ")

    for usuario in usuarios:
        if usuario['nombre_usuario'] == nombre_usuario and usuario['rol'] == 'profesor':
            if 'calificaciones' in usuario:
                for calificacion in usuario['calificaciones']:
                    if calificacion['alumno'] == alumno and calificacion['asignatura'] == asignatura:
                        print(f"Calificación actual: {calificacion['calificacion']}")
                        nueva_calificacion = input("Ingrese la nueva calificación (deje en blanco para mantenerla igual): ")
                        if nueva_calificacion:
                            calificacion['calificacion'] = nueva_calificacion

                            with open('usuarios.json', 'w') as file:
                                json.dump({'usuarios': usuarios}, file, indent=4)
                            print("Calificación modificada con éxito.")
                        else:
                            print("La calificación no se modificó.")
                        return

            print("No se encontró la calificación.")
            return

    print("No se encontró al profesor.")


# Programa principal
def main():
    print("Sistema de Gestión de Calificaciones")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    rol = autenticar_usuario(nombre_usuario, contrasena)

    if rol:
        mostrar_perfil(rol)
    else:
        print("Credenciales incorrectas. Inicie sesión nuevamente.")

    while True:
        print("\nMENU")
        print("1. Registrar Calificación")
        print("2. Consultar y Modificar Calificaciones")
        print("3. Registrar Alumno")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        usuarios = cargar_datos()

        if opcion == "1":
            registrar_calificacion(usuarios, nombre_usuario)
        elif opcion == "2":
            consultar_y_modificar_calificaciones(usuarios, nombre_usuario)
        elif opcion == "3":
            #registrar_alumno(usuarios)
        #elif opcion == "4":
            print("Saliendo del menú.")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
    while True:
        print("\nMENU")
        print("1. Registrar Calificación")
        print("2. Consultar y Modificar Calificaciones")
        print("3. Ver Mis Calificaciones")
        print("4. Registrar Alumno")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_calificacion(usuarios, nombre_usuario)
        elif opcion == "2":
            consultar_y_modificar_calificaciones(usuarios, nombre_usuario)
        elif opcion == "3":
            ver_calificaciones_alumno(usuarios, nombre_usuario)
        elif opcion == "4":
           # registrar_alumno(usuarios)
        #elif opcion == "5":
            print("Saliendo del menú.")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
