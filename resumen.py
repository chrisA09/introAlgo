# utility

# validar rango

def validarEnRango(li,ls,cf,texto):
    valor = int(input(texto))
    while (valor<li or valor>ls) and valor != cf:
        valor = int(input(texto))
    return valor

print(validarEnRango(10,100,-1,"ingrese valor"))

# listas en paralelo

cant = int(input("ingrese la cantidad de alumnos del curso"))

legajo = [0]*cant
nota = [0]*cant

for i in range(cant):
    legajo[i] = int(input("ingrese legajo"))
    nota[i] = int(input("ingrese una nota"))

for i in range(cant):
    print(legajo[i], "  nota-->  ", nota[i])

# busqueda de maximo y minimo unico!

lista = [1000,5999,2500,4200,3244]

for i in range(len(lista)):
    if i == 0 or lista[i]>maximo:
        maximo=lista[i]

print(maximo)

# busqueda de posicion de un maximo

lista = [1000,5999,2500,4200,3244]

for i in range(len(lista)):
    if i == 0 or lista[i] > maximo:
        maximo = lista[i]
        posicion = i
    
print(maximo,"  en la posicion", posicion)

# func busqueda secuencial

def busqueda(lista, valor_buscado):
    pos = -1
    i = 0

    while(pos == -1 and i < len(lista)):
        if (lista[i] == valor_buscado):
            pos = i
        i = i +1

    return pos

# func ordenamiento por burbujeo


def bubble_sort_listas_relacionadas(lista1,lista2):

    for i in range(0, len(lista1)-1):
        for j in range(0,len(1)-1-i):
            if (lista1[j] > lista1[j+1]):
                aux = lista1[j]
                lista1[j] = lista1[j+1]
                lista1[j+1] = aux

                aux = lista2[j]
                lista2[j] = lista2[j+1]
                lista2[j+1] = aux