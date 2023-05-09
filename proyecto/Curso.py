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

    def getCurso(self):
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
                print('❃❃❃❃❃❃❃❃❃❃\n')
        except Exception as e:
            print('Error: ', e)  
            raise 

    def getCurso_ID(self):
        pass

    

    def deleteCurso(self, id):
        sql= "DELETE FROM `curso`WHERE id='{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(f"Se ha eliminado el registro: {id}")
        except Exception as e:
            print('Error: ',e)
            raise