'''
Clase con funciones relacionadas al manejo de los datos en la base de datos de Curso.
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

    def getCurso(self):#Funcion para obtener todos los registros
        sql= 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso'
        try:
            self.cursor.execute(sql)
            curso= self.cursor.fetchall()
            for item in curso:
                print("ID", item[0])
                print("Nombre", item[1])
                print("Descripcion", item[2])
                print("Tiempo", item[3])
                print("Usuario", item[4])
                print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print('Error: ', e)  
            raise 

    def getCurso_ID(self, id):#Funcion para obtener un registro especifico
        sql = "SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            curso = self.cursor.fetchone()
            print("ID", curso[0])
            print("Nombre", curso[1])
            print("Descripcion", curso[2])
            print("Tiempo", curso[3])
            print("Usuario", curso[4])
            print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print('Error: ', e )
            raise

#Funciones para actualizar elementos de los registros
    def updateCurso_ID(self, id, nombre):
        sql = "UPDATE curso SET nombre='{}' WHERE id='{}'".format(nombre, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el nombre del registro: {id}\n")
        except Exception as e:
            print('Error: ', e )
            raise

    def updateCurso_TimeID(self, id, tiempo):
        sql = "UPDATE curso SET tiempo='{}' WHERE id='{}'".format(tiempo, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha actualizado el tiempo del registro: {id}\n")
        except Exception as e:
            print('Error: ', e )
            raise

    def updateCurso_TotalID(self, id, nombre, descripcion, tiempo, usuario):
        sql = "UPDATE curso SET nombre='{}', descripcion='{}', tiempo='{}', usuario='{}' WHERE id='{}'".format(nombre, descripcion, tiempo, usuario, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se han actualizado todos los datos del registro: {id}\n")
        except Exception as e:
            print('Error: ', e )
            raise 

    def createCurso(self, nombre, descripcion, tiempo, usuario):#Funcion para crear un nuevo registro
        sql = "INSERT INTO curso(id, nombre, descripcion, tiempo, usuario) VALUES ('{}','{}','{}','{}','{}')".format(0, nombre, descripcion, tiempo, usuario)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se ha creado un nuevo registro\n")
        except Exception as e:
            print('Error: ', e )
            raise

    def deleteCurso(self, id):#Funcion para eliminar un registro
        sql= "DELETE FROM `curso`WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha eliminado el registro: {id}\n")
        except Exception as e:
            print('Error: ',e)
            raise