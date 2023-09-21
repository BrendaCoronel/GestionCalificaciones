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

if __name__ == "__main__":
    main()
