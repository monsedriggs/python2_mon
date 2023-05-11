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
                print("Fecha de Nacimiento", item[4])
                print("Sexo", item[5])
                print("Direccion", item[6])
                print("Nombre", item[7])
                print("Apellido Paterno", item[8])
                print("Apellido Materno", item[9])
                print("Nacionalidad", item[10])
                print("ID Carreras", item[11])
                print("Usuario", item[12])
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
            print("Fecha de Nacimiento", student[4])
            print("Sexo", student[5])
            print("Direccion", student[6])
            print("Nombre", student[7])
            print("Apellido Paterno", student[8])
            print("Apellido Materno", student[9])
            print("Nacionalidad", student[10])
            print("ID Carreras", student[11]) 
            print("Usuario", student[12])
            print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print("Error: ", e)
            raise