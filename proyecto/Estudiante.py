'''
Clase con funciones relacionadas al manejo de los datos en la base de datos de Estudiante.
Obtener todos los registros, uno en especifico, actualizar cada uno de los elementos en la base de datos o todos (de un registro especifico), crear un nuevo registro o eliminar uno
'''
import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )
        self.cursor = self.connection.cursor()
        print('\tConectada a la base de datos\n')

    def getStudent(self):
        sql= 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante'
        try:
            self.cursor.execute(sql)
            student=self.cursor.fetchall()
            for item in student:
                print("ID", item[0])
                print("Cedula", item[1])
                print("Correo electrónico", item[2])
                print("Telefono", item[3])
                print("Telefono Celular", item[4])
                print("Fecha de Nacimiento", item[5])
                print("Sexo", item[6])
                print("Direccion", item[7])
                print("Nombre", item[8])
                print("Apellido Paterno", item[9])
                print("Apellido Materno", item[10])
                print("Nacionalidad", item[11])
                print("ID Carreras", item[12])
                print("Usuario", item[13])
                print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print("Error: ", e)
            raise

    def getStudent_ID(self, id):
        sql= 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante WHERE id={}'.format(id)
        try:
            self.cursor.execute(sql)
            student=self.cursor.fetchone()
            print("ID", student[0])
            print("Cedula", student[1])
            print("Correo electrónico", student[2])
            print("Telefono", student[3])
            print("Telefono Celular", student[4])
            print("Fecha de Nacimiento", student[5])
            print("Sexo", student[6])
            print("Direccion", student[7])
            print("Nombre", student[8])
            print("Apellido Paterno", student[9])
            print("Apellido Materno", student[10])
            print("Nacionalidad", student[11])
            print("ID Carreras", student[12]) 
            print("Usuario", student[13])
            print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print("Error: ", e)
            raise

    def updateStudent_ID(self, id, nombre):
        sql="UPDATE estudiante SET nombre='{}' WHERE id='{}'".format(nombre,id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_CedulaID(self, id, cedula):
        sql="UPDATE estudiante SET cedula='{}' WHERE id='{}'".format(cedula, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_CorreoID(self, id, correo_electronico):
        sql="UPDATE estudiante SET correo_electronico='{}' WHERE id='{}'".format(correo_electronico, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_TelefonoID(self, id, telefono):
        sql= "UPDATE estudiante SET telefono='{}' WHERE id='{}'".format(telefono, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_TelCelularID(self, id, telefono_celular):
        sql="UPDATE estudiante SET telefono_celular='{}' WHERE id='{}'".format(telefono_celular, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_FechaNacimientoID(self, id, fecha_nacimiento):
        sql= "UPDATE estudiante SET fecha_nacimiento='{}' WHERE id='{}'".format(fecha_nacimiento, id)
        try: 
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error. ', e)
            raise

    def updateStudent_SexoID(self, id, sexo):
        sql="UPDATE estudiante SET sexo='{}' WHERE id='{}'".format(sexo, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_DireccionID(self, id, direccion):
        sql="UPDATE estudiante SET direccion='{}' WHERE id='{}'".format(direccion, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_ApellidoPaternoID(self, id, apellido_paterno):
        sql="UPDATE estudiante SET apellido_paterno='{}' WHERE id='{}'".format(apellido_paterno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_ApellidoMaternoID(self, id, apellido_materno):
        sql="UPDATE estudiante SET apellido_materno='{}' WHERE id='{}'".format(apellido_materno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_NacionalidadID(self, id, nacionalidad):
        sql= "UPDATE estudiante SET nacionalidad='{}' WHERE id='{}'".format(nacionalidad, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_CarrerasID(self, id, id_carreras):
        sql= "UPDATE estudiante SET id_carreras='{}' WHERE id='{}'".format(id_carreras, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_UsuarioID(self, id, usuario):
        sql= "UPDATE estudiante SET usuario='{}' WHERE id='{}'".format(usuario, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateStudent_TotalID(self, id, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, id_carreras, usuario):
        sql = "UPDATE estudiante SET cedula='{}', correo_electronico='{}', telefono='{}', telefono_celular='{}', fecha_nacimiento='{}', sexo='{}', direccion='{}', nombre='{}', apellido_paterno='{}', apellido_materno='{}', nacionalidad='{}', id_carreras='{}', usuario='{}'WHERE id='{}'".format(cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, id_carreras, usuario, id) 
        try:
            self.cursor. execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ',  e)
            raise

    def createStudent(self, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, id_carreras, usuario):
        sql= "INSERT INTO estudiante(id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario) VALUES ('{}','{}','{}','{}','{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}')".format(0, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, id_carreras, usuario)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise

    def deleteStudent(self, id):
        sql= "DELETE FROM `estudiante`WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha eliminado el registro: {id}")
        except Exception as e:
            print("Error: ", e)
            raise