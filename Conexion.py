import psycopg2

class Conexion:

    @staticmethod
    def listarPersonas():
        try:
            conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',
                                        database='personas')
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "SELECT * FROM persona"
                    cursor.execute(sentencia)
                    registros = cursor.fetchall()
                    for registro in registros:
                        print(registro)
        except Exception as ex:
            print(f"Ocurrio una excepcion: {ex}")
        finally:
            conexion.close()

    @staticmethod
    def ingresarPersona(datos):
        try:
            conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',
                                        database='personas')
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "INSERT INTO persona (nombre, apellido, edad, email) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sentencia, datos)
        except Exception as ex:
            print(f"Ocurrio una excepcion: {ex}")
        finally:
            conexion.close()

    @staticmethod
    def eliminarRegistro(idPersona):
        try:
            conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',
                                        database='personas')
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "DELETE FROM persona WHERE id_persona = %s"
                    cursor.execute(sentencia, idPersona)
                    cantRegistrosModificados = cursor.rowcount
                    print(f"Cantidad de registros eliminados: {cantRegistrosModificados}")
        except Exception as ex:
            print(f"Ocurrio una excepcion: {ex}")
        finally:
            conexion.close()

    @staticmethod
    def actualizarRegistro(datos):
        try:
            conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',
                                        database='personas')
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "UPDATE persona SET nombre = %s, apellido = %s, edad = %s, email = %s  WHERE id_persona = %s"
                    cursor.execute(sentencia, datos)
                    cantRegistrosModificados = cursor.rowcount
                    print(f"Cantidad de registros modificados: {cantRegistrosModificados}")
        except Exception as ex:
            print(f"Ocurrio una excepcion: {ex}")
        finally:
            conexion.close()

    @staticmethod
    def buscarPorId(idPersona):
        try:
            conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',
                                        database='personas')
            with conexion:
                with conexion.cursor() as cursor:
                    sentencia = "SELECT * FROM persona WHERE id_persona = %s"
                    cursor.execute(sentencia, idPersona)
                    registro = cursor.fetchone()
                    print(registro)
        except Exception as ex:
            print(f"Ocurrio una excepcion: {ex}")
        finally:
            conexion.close()