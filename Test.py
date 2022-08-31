from Conexion import Conexion

def menu():
    try:
        op = 0
        while op != 6:
            print("""
                1_Ingresar persona
                2_Listar personas
                3_Eliminar persona
                4_Buscar persona por ID
                5_Actualizar persona
                6_salir
                """)
            op = int(input("Ingrese su opcion: "))
            if op == 1:
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                edad = int(input("Ingrese edad: "))
                email = input("Ingrese email: ")
                datos = (nombre, apellido, edad, email)
                Conexion.ingresarPersona(datos)
            elif op == 2:
                Conexion.listarPersonas()
            elif op == 3:
                idPersona = input("Ingrese id de la persona a eliminar: ")
                Conexion.eliminarRegistro(idPersona)
            elif op == 4:
                idPersona = input("Ingrese el id de la persona a buscar: ")
                Conexion.buscarPorId(idPersona)
            elif op == 5:
                idPersona = input("Ingrese id de la persona a modificar: ")
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                edad = int(input("Ingrese edad: "))
                email = input("Ingrese email: ")
                datos = (nombre, apellido, edad, email, idPersona)
                Conexion.actualizarRegistro(datos)
            elif op == 6:
                print("Adios...")
            else:
                print("Opcion incorrecta")
    except Exception as ex:
        print(f"Ocurrio una excepcion: {ex}")

menu()
