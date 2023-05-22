'''
Clase con funciones relacionadas al manejo de los datos en la base de datos de Profesor.
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
    
    def getProfe(self):#Funcion para obtener todos los registros
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

    def getProfe_ID(self, id):#Funcion para obtener un registro especifico
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

#Funciones para actualizar elementos de los registros
    def updateProfe_ID(self, id, nombre):
        sql="UPDATE estudiante SET nombre='{}' WHERE id='{}'".format(nombre,id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el nombre del registro: {id}\n")
        except Exception as e:
            print("Error: ", e)
            raise

    def updateProfe_CedulaID(self, id, cedula):
        sql="UPDATE profesor SET cedula='{}' WHERE id='{}'".format(cedula, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado la cedula del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_CorreoID(self, id, correo_electronico):
        sql="UPDATE profesor SET correoelectronico='{}' WHERE id='{}'".format(correo_electronico, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el correo del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_TelefonoID(self, id, telefono):
        sql="UPDATE profesor SET telefono='{}' WHERE id='{}'".format(telefono, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el telefono del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise
        
    def updateProfe_TelCelularID(self, id, telefono_celular):
        sql="UPDATE profesor SET telefonocelular='{}' WHERE id='{}'".format(telefono_celular, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el celular del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_FechaNacimientoID(self, id, fecha_nacimiento):
        sql="UPDATE profesor SET fechanacimiento='{}' WHERE id='{}'".format(fecha_nacimiento, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado la fecha de nacimiento del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_SexoID(self, id, sexo):
        sql="UPDATE profesor SET sexo='{}' WHERE id='{}'".format(sexo, id)
        try:
            self.cursor.execute(sql)
            self.conncetion.commit()
            print(f"Se ha actualizado el sexo del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_DireccionID(self, id, direccion):
        sql="UPDATE profesor SET direccion='{}' WHERE id='{}'".format(direccion, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado la direccion del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_ApellidoPaternoID(self, id, apellido_paterno):
        sql="UPDATE profesor SET apellidopaterno='{}' WHERE id='{}'".format(apellido_paterno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el apellido paterno del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def updateProfe_ApellidoMaternoID(self, id, apellido_materno):
        sql="UPDATE profesor SET apellidomaterno='{}' WHERE id='{}'".format(apellido_materno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el apellido materno del registro: {id}\n")
        except Exception as e:
            print('Error: ',e)
            raise
            
    def updateProfe_NacionalidadID(self, id, nacionalidad):
        sql="UPDATE profesor SET nacionalidad='{}' WHERE id='{}'".format(nacionalidad, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado la nacionalidad del registro: {id}\n")
        except Exception as e:
            print("Error: ", e)
            raise

    def updateProfe_CarrerasID(self, id, id_carreras):
        sql="UPDATE profesor SET idcarreras='{}' WHERE id='{}'".format(id_carreras, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el ID de carreras del registro: {id}\n")
        except Exception as e:
            print("Error: ", e)
            raise

    def updateProfe_UsuarioID(self, id, usuario):
        sql="UPDATE profesor SET usuario='{}' WHERE id='{}'".format(usuario, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el usuario del registro: {id}\n")
        except Exception as e:
            print("Error: ", e)
            raise

    def updateProfe_TotalID(self, id, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, usuario, id_carreras):
        sql="UPDATE profesor SET cedula='{}',correoelectronico='{}',telefono='{}',telefonocelular='{}',fechanacimiento='{}',sexo='{}',direccion='{}',nombre='{}',apellidopaterno='{}',apellidomaterno='{}',nacionalidad='{}',usuario='{}',idcarreras='{}' WHERE id='{}'".format(cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, usuario, id_carreras, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se han actualizado todos los datos del registro: {id}\n")
        except Exception as e:
            print('Error: ', e)
            raise

    def createProfe(self, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, usuario, id_carreras ):
        #Funcion para crear un nuevo registro
        sql="INSERT INTO profesor(id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(0, cedula, correo_electronico, telefono, telefono_celular, fecha_nacimiento, sexo, direccion, nombre, apellido_paterno, apellido_materno, nacionalidad, usuario, id_carreras)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se ha creado un nuevo registro\n")
        except Exception as e:
            print('Error: ', e )
            raise

    def deleteProfe(self, id):#Funcion para eliminar un registro
        sql= "DELETE FROM `profesor`WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha eliminado el registro: {id}\n")
        except Exception as e:
            print('Error: ',e)
            raise