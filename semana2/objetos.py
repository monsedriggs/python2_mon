from datetime import datetime

#Personas
#Clase persona, atributos y funciones
class Persona:
#Primero se crea el inicializador de los datos
    def __init__(self, nombre, apellido, email, nacimiento, telefono, provincia):
        self.nombre = nombre
        self.apellido= apellido
        self.email= email
        self.nacimiento= nacimiento
        self.telefono= telefono
        self.provincia= provincia
#Creo la funcion que muestre los datos        
    def getNombre(self):
        print(self.nombre)

#Cambiar o ajustar los datos
    def setNombre( self, nombre):
        self.nombre = nombre

#Se requieren los set y gets email, apellido, fecha nacimiento, telefono, provincia 
    def getApellido(self):
        print(self.apellido) 
    def setApellido(self, apellido):
        self.apellido= apellido

    def getEmail(self):
        print(self.email)
    def setEmail(self, email):
        self.email= email

    def getNacimiento(self):
        print(self.nacimiento)
    def setNacimiento(self, nacimiento):
        self.nacimiento= nacimiento

    def getNumber(self):
        print(self.telefono)
    def setNumber(self, telefono):
        self.telefono= telefono

    def getProvincia(self):
        print(self.provincia)
    def setProvincia(self, provincia):
        self.provincia= provincia

#Se requiere una funcion que calcule la edad, con base a la fecha de nacimeiento
    def calcular_edad(self):
        actual= datetime.now()
        formato= "%d/%m/%Y"
        nacimiento= datetime.strptime(self.nacimiento, formato)
        diferencia= actual- nacimiento
        print(f"{diferencia.days //365}")
        
#se necesita una funcion que imprima toda la informacion agregada.
    def mostrar(self):
        print("Nombre: ");self.getNombre()
        print("\nApellido: ");self.getApellido()
        print("\nEmail: ");self.getEmail()
        print("\nNacimiento:");self.getNacimiento()
        print("\nEdad: "); self.calcular_edad()
        print("\nNumero Telefono: ");self.getNumber()
        print("\nProvincia: ");self.getProvincia()
#Fin de la clase

Usuario = Persona("Monse","Aguilar", "monsedriggs@gmail.com", "10/04/2002", "72739479", "Heredia")
Usuario.mostrar()