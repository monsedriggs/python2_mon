def calcular_suma(num1, num2):
    return num1+num2

def calcular_resta(num1, num2):
    return num1-num2

def calcular_multiplicacion(num1, num2):
    return num1*num2

def calcular_division(num1, num2):
    return num1//num2

def calcular_tabla_multiplicar(num1, num2):
    for num in range(0,num2, +1):
        print(f"{num1}x{num}= {num1*num}")


def correr():
    while True:
        opcion= int(input("\t1)Suma\n\t2)Resta\n\t3)Multiplicacion\n\t4)Division\n\t5)Tabla de Multiplicar\n\t6)Salir\nSeleccione una opcion: "))
        if opcion==1:
            num_sum1=int(input("Ingrese el primer numero que desee sumar: "))
            num_sum2=int(input("Ingrese el segundo numero que desea sumar: "))
            suma= calcular_suma(num_sum1, num_sum2)
            print(f"El resultado de la suma es: {suma}")
        elif opcion==2:
            num_minuendo=int(input("Ingrese el minuendo: "))
            num_sustraendo=int(input("Ingrese el sustraendo: "))
            resta= calcular_resta(num_minuendo,num_sustraendo)
            print(f"El resultado de la resta es: {resta}")
        elif opcion==3:
            num_mult1=int(input("Ingrese el primer factor: "))
            num_mult2= int(input("Ingrese el segundo factor:  "))
            multiplicacion= calcular_multiplicacion(num_mult1, num_mult2)
            print(f"El producto es: {multiplicacion}")
        elif opcion==4:
            num_dividendo= int(input("Digite el dividendo: "))
            num_divisor= int(input("Digite el divisor: "))
            division= calcular_division(num_dividendo, num_divisor)
            print(f"El resultado de la division es: {division}")
        elif opcion==5:
            num_tabla= int(input("Indique el numero de la tabla de multiplicar que desea ver: "))
            num_multiplicador= int(input("Ingrese hasta qué numero desea multiplicar: "))
            tabla_multiplicar= calcular_tabla_multiplicar(num_tabla, num_multiplicador)
            print(tabla_multiplicar)
        elif opcion==6:
            print("Gracias!")
            break
        else:
            print("Error, opcion invalida")
    
correr()