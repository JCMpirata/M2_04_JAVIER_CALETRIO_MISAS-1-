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


