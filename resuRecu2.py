"""
1) Desarrolle una función cargaLista que reciba una lista vacía y genere 
10 códigos al azar correspondiente a las estaciones meteorológicas. 
Estos códigos deben ser valores numéricos enteros entre 100 y 500 y no 
pueden encontrarse duplicados.
2) Desarrolle una función cargaMediciones que defina dentro de la función 
una lista vacía y la cargue en forma aleatoria con valores entre 0 a 200 
representado los mm caídos y medidos por cada estación 
meteorológica. 
3) Desarrolle una función mostrarDatos que reciba ambas listas y muestre 
el siguiente listado:
MEDICIONES LLUVIAS CAIDAS
ESTACION   MM CAIDOS
XXX          XX
XXX           X
…            ...
XXX          XXX
4) Sin ordenar las listas, calcule el máximo y el mínimo valor de lluvia 
caída, informe que estación midió estos valores.
5) Ordenar las listas en forma ascendente por milímetros caídos. Luego de 
ordenar volver a llamar a la función mostrarDatos para visualizar 
nuevamente el listado.
6) Realizar una consulta a la lista de la siguiente manera: Se le pide al 
usuario que ingrese un valor de lluvia caída, y debe buscarlo con 
búsqueda binaria informando si esa medición se encuentra o no dentro 
de la lista. Si se encuentra informar a que estación pertenece la 
medición. (PUNTO PARA FINAL REGULAR/ADELANTADO)
7) Realizar una consulta a la lista de la siguiente manera:
Se le pide al 
usuario que ingrese un valor de lluvia caída, y debe buscarlo
informando 
si esa medición se encuentra o no dentro de la lista.
Si se encuentra 
informar a que estación pertenece la medición. (PUNTO PARA 
RECUPERATORIO"""

import random

def ordenamiento(lista1, lista2):
    for i in range(len(lista1)-1):
        for j in range(len(lista1)-1-i):
            if (lista1[j] > lista1[j+1]):
                aux = lista1[j]
                lista1[j] = lista1[j+1]
                lista1[j+1] = aux
                
                aux = lista2[j]
                lista2[j] = lista2[j+1]
                lista2[j+1] = aux
                
def busqueda_binaria(lista, valor_buscado):
  posicion = -1
  izq = 0
  der = len(lista)-1
  while (posicion == -1 and izq <= der):
    medio = (izq + der) // 2
    if (lista[medio] == valor_buscado):
      posicion = medio
    else:
      #Mi valor buscado puede estar a la derecha del medio
      if (valor_buscado > lista[medio]):
        izq = medio + 1
      else:
        # Si el valor buscado esta a la izquierda del medio
        der = medio - 1
  return posicion

def busqueda(li,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(li):
        if li[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def cargaLista(lista):
    
    while len(lista)<10:
        valor=random.randint(100,500)
        pos=busqueda (lista,valor)
        if pos==-1:
            lista.append(valor)

def cargaMediciones():
    lista=[]
    for i in range(10):
        lista.append(random.randint(0,200))
    return lista

def mostrarDatos(listaE,listaM):
    print("MEDICIONES LLUVIAS CAIDAS")
    print("ESTACION   MM CAIDOS")
    
    for i in range(len(listaE)):
        print(listaE[i],"\t",listaM[i])
    
def maximo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i]>valorMaximo:
            valorMaximo=lista[i]
            posMaximo = i
    return posMaximo
    
def minimo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i]<valorMinimo:
            valorMinimo=lista[i]
            posMinimo = i
    return posMinimo
    

# comienza el programa principal
ESTACIONES=[]
cargaLista(ESTACIONES)
print(ESTACIONES)


MEDICIONES=cargaMediciones()
print(MEDICIONES)

mostrarDatos(ESTACIONES, MEDICIONES)

posMAX=maximo(MEDICIONES)
posMIN=minimo(MEDICIONES)

print("La estacion que reporto el valor maximo es ", ESTACIONES[posMAX])
print("La estacion que reporto el valor minimo es ", ESTACIONES[posMIN])

ordenamiento(MEDICIONES, ESTACIONES)
mostrarDatos(ESTACIONES, MEDICIONES)


valor=int(input("Ingrese una medicion a buscar SECUENCIAL"))
pos=busqueda(MEDICIONES,valor)
if pos==-1:
    print("MEDICION INCORRECTA")
else:
    print("La estacion que midio esta precipitacion es ", ESTACIONES[pos])
    
valor=int(input("Ingrese una medicion a buscar BINARIA"))
pos=busqueda_binaria(MEDICIONES,valor)
if pos==-1:
    print("MEDICION INCORRECTA")
else:
    print("La estacion que midio esta precipitacion es ", ESTACIONES[pos])



valor=int(input("ACTUALIZACION Ingrese una estacion a buscar"))
pos=busqueda(ESTACIONES,valor)
if pos==-1:
    print("ESTACION INCORRECTA")
else:
    mm=int(input("Ingrese cantidad de mm caidos "))
    
    MEDICIONES[pos]+=mm
    
    
    
