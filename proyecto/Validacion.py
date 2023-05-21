'''
Función para validar si la entrada del usuario está vacía o solo son espacios.
'''

def validar_input(entrada, funcion):
    if entrada.isspace() or len(entrada)==0:
        print("Error, debe escribir algo\n")
    else:
        return funcion