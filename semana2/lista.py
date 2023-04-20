# Esto es un arreglo de datos
mylista = [0,1,2,3,4,5]

direccion ={
    'Direccion':"Costa Rica", 
    'Provincia':'SJ', 
    'Canton':'SJ', 
    'Ciudad':'Sabana'
}

diccionarioJson = {
    'nombre' : 'Mario',
    'Apellido' : 'Jimenez',
    'Telefono' : '61383453',
    'MyLista': [0,1,2,3,4,5],
    'Direccion': direccion
}


print (mylista)

print(diccionarioJson['nombre'])


for keylista in diccionarioJson:
    print('Keylista: ', diccionarioJson[keylista])
