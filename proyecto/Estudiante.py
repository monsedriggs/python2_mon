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