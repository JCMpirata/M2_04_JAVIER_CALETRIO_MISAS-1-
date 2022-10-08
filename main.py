#EJERCICIO 1
#LISTA
paises = ["España", "Alemania", "Italia", "Suiza", "Francia", "Inglaterra"]
print(paises)
#Segundo elemento
print(f"El segundo elemento es: ", paises[1])
#Longitud de la lista
print(f"La lista mide: ", len(paises))
#Busqueda en la lista
print(f"Queremos buscar: ", paises[3])
#Añadir elemento
paises.insert(3, "Austria")
print(paises)
#Eliminar elemento
paises.remove("Inglaterra")
print(paises)

#Tupla
ciudades = ("Madrid", "Stuttgart", "Munich", "Paris", "Florencia", "Viena")
print(ciudades)
#Penultimo elemento
print(f"El penultimo elemento es: ", ciudades[4])
#Longitud de l tupla
print(f"La tupla mide: ", len(ciudades))
#Busqueda en la tupla
print(f"Queremos buscar: ", ciudades[1])
#Añadir elemento
#A diferencia de las listas, en las tuplas no podemos añadir elementos, ya que no existe esa posibilidad.
#Elimanar elemento
# A diferencia de las listas, en las tuplas no podemos eliminar elentos, ya que no existe esa posibilidad.

print("\n")

#Ejercico 2
#Diccionario
baseDeDatos = {"Nombre": "Javier", "Apellido": "Caletrio",   "Pais": "España"}
print(baseDeDatos)
#Primer valor - clave
print(baseDeDatos["Nombre"][0:6])
#Longitud diccionario
print(f"El diccionario mide: ", len(baseDeDatos.keys()))
#Añadir elemento
baseDeDatos["Gate"] = "D16"
print(baseDeDatos)
#Eliminar elemento
del(baseDeDatos["Apellido"])
print(baseDeDatos)

#SET








