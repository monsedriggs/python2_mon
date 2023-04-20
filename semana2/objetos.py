from datetime import datetime
import re

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
        print(f"Nombre: {self.nombre}")

#Cambiar o ajustar los datos
    def setNombre( self, nombre):
        self.nombre = nombre

#Se requieren los set y gets email, apellido, fecha nacimiento, telefono, provincia 
    def getApellido(self):
        print(f"Apellido: {self.apellido}") 
    def setApellido(self, apellido):
        self.apellido= apellido

    def getEmail(self):
        print(f"Email: {self.email}")
    def setEmail(self, email):
        self.email= email
    def verificarEmail(self):
        buscador= re.search("@cursopython.com", self.email)
        if buscador:
            print("Email válido")
        else:
            print("Email inválido")

    def getNacimiento(self):
        print(f"Nacimiento: {self.nacimiento}")
    def setNacimiento(self, nacimiento):
        self.nacimiento= nacimiento

    def getNumber(self):
        print(f"Numero: {self.telefono}")
    def setNumber(self, telefono):
        self.telefono= telefono

    def getProvincia(self):
        print(f"Provincia: {self.provincia}")
    def setProvincia(self, provincia):
        self.provincia= provincia

#Se requiere una funcion que calcule la edad, con base a la fecha de nacimeiento
    def calcular_edad(self):
        actual= datetime.now()
        formato= "%d/%m/%Y"
        nacimiento= datetime.strptime(self.nacimiento, formato)
        diferencia= actual- nacimiento
        print(f"Edad: {diferencia.days //365}")
        
#se necesita una funcion que imprima toda la informacion agregada.
    def mostrar(self):
        print(self.getNombre(), self.getApellido(), self.getEmail(), self.verificarEmail(), self.getNacimiento(), self.calcular_edad(), self.getNumber(), self.getProvincia())      
#Fin de la clase

Usuario = Persona("Monse","Aguilar", "monsedriggs@cursopython.com", "10/04/2002", "72739479", "Heredia")
Usuario.mostrar()