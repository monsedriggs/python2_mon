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
        pass

    def updateStudent_CedulaID(self, id, cedula):
        pass

    def updateStudent_CorreoID(self, id, correo_electronico):
        pass

    def updateStudent_TelefonoID(self, id, telefono):
        pass

    def updateStudent_TelCelularID(self, id, telefono_celular):
        pass

    def updateStudent_FechaNacimientoID(self, id, fecha_nacimiento):
        pass

    def updateStudent_SexoID(self, id, sexo):
        pass

    def updateStudent_DireccionID(self, id, direccion):
        pass

    def updateStudent_ApellidoPaternoID(self, id, apellido_paterno):
        pass

    def updateStudent_ApellidoMaternoID(self, id, apellido_materno):
        pass

    def updateStudent_NacionalidadID(self, id, nacionalidad):
        pass

    def updateStudent_CarrerasID(self, id, id_carreras):
        pass

    def updateStudent_UsuarioID(self, id, usuario):
        pass

    def updateStudent_TotalID(self, id, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, id_carreras, usuario):
        pass

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