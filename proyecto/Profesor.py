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
    
    def getProfe(self):
        sql= 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor'
        try:
            self.cursor.execute(sql)
            professor= self.cursor.fetchall()
            for item in professor:
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
                print("Usuario", item[12])
                print("ID Carreras", item[13])
                print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print('Error: ', e )
            raise

    def getProfe_ID(self, id):
        sql= 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor WHERE id={}'.format(id)
        try:
            self.cursor.execute(sql)
            professor= self.cursor.fetchone()
            print("ID", professor[0])
            print("Cedula", professor[1])
            print("Correo electrónico", professor[2])
            print("Telefono", professor[3])
            print("Telefono Celular", professor[4])
            print("Fecha de Nacimiento", professor[5])
            print("Sexo", professor[6])
            print("Direccion", professor[7])
            print("Nombre", professor[8])
            print("Apellido Paterno", professor[9])
            print("Apellido Materno", professor[10])
            print("Nacionalidad", professor[11])
            print("Usuario", professor[12])
            print("ID Carreras", professor[13]) 
            print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print('Error: ', e )
            raise

    def updateProfe_ID(self, id, nombre):
        sql="UPDATE profesor SET nombre='{}' WHERE id'{}'".format(nombre, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("Error: ", e)
            raise

    def updateProfe_CedulaID(self, id, cedula):
        sql="UPDATE profesor SET cedula='{}' WHERE id='{}'".format(cedula, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_CorreoID(self, id, correo_electronico):
        sql="UPDATE profesor SET correo_electronico='{}' WHERE id='{}'".format(correo_electronico, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_TelefonoID(self, id, telefono):
        pass

    def updateProfe_TelCelularID(self, id, telefono_celular):
        pass

    def updateProfe_FechaNacimientoID(self, id, fecha_nacimiento):
        pass

    def updateProfe_SexoID(self, id, sexo):
        sql="UPDATE profesor SET sexo='{}' WHERE id='{}'".format(sexo, id)
        try:
            self.cursor.execute(sql)
            self.conncetion.commit()
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_DireccionID(self, id, direccion):
        pass

    def updateProfe_ApellidoPaternoID(self, id, apellido_paterno):
        pass

    def updateProfe_ApellidoMaternoID(self, id, apellido_materno):
        pass

    def updateProfe_NacionalidadID(self, id, nacionalidad):
        pass

    def updateProfe_CarrerasID(self, id, id_carreras):
        pass

    def updateProfe_UsuarioID(self, id, usuario):
        pass

    def updateProfe_TotalID(self, id, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, usuario, id_carreras):
        pass

    def createProfe(self, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, usuario, id_carreras ):
        sql="INSERT INTO profesor(id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(0, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, usuario, id_carreras)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise

    def deleteProfe(self, id):
        sql= "DELETE FROM `profesor`WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha eliminado el registro: {id}")
        except Exception as e:
            print('Error: ',e)
            raise