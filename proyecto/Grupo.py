'''
Clase con funciones relacionadas al manejo de los datos en la base de datos de Grupo.
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

    def getGroup(self):#Funcion para obtener todos los registros
        sql= 'SELECT id, nombre FROM grupo' 
        try:
            self.cursor.excute(sql)
            grupo=self.cursor.fetchall()
            for item in grupo:
                print("ID", item[0])
                print("Nombre", item[1])
                print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print('Error: ', e)  
            raise 

    def getGroup_ID(self, id):#Funcion para obtener un registro especifico
        sql= 'SELECT id, nombre FROM grupo WHERE id={}'.format(id)
        try:
            self.cursor.excute(sql)
            grupo=self.cursor.fetchone()
            print("ID", grupo[0])
            print("Nombre", grupo[1])
            print('❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃ ❃\n')
        except Exception as e:
            print('Error: ', e)  
            raise

    def uptadeGroup_ID(self, id, nombre):#Funciones para actualizar elementos de los registros
        sql= "UPDATE grupo SET nombre='{}' WHERE id='{}'".format(nombre, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("Error: ", e)
            raise

    def createGroup(self, nombre):#Funcion para crear un nuevo registro
        sql= "INSERT INTO grupo(id, nombre) VALUES ('{}','{}')".format(0, nombre)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('Error: ', e )
            raise

    def deleteGroup(self,id):#Funcion para eliminar un registro
        sql= "DELETE FROM `group`WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha eliminado el registro: {id}")
        except Exception as e:
            print('Error: ',e)
            raise