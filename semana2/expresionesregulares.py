import re

txt = "Clase 19 Abril nuevas clases 2024"
#Impr normal
print(txt)
#Buscando palabras
buscardor = re.search("^Clase.*Abril", txt)
print(buscardor)

#Muestras las concidencias que encuentra con la palabra
print(re.findall("se",txt))

#Split
print(re.split("\s", txt))

#replace data, remplaza el caracter buscado, por uno seleccionado por el usuario
print(re.sub("a", '--------------' , txt))

evaluacion = re.search("^Clase.*Abril", txt)
print(evaluacion.span())

