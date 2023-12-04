import random

# carga

'''
funcion que crea y devuelve una lista con 10 valores random de 0 a 200

'''

def cargaMediciones():
    lista=[]
    for i in range(10):
        lista.append(random.randint(0,200))
    return lista

# carga con verificacion de duplicado

def cargaInicial(lc,lp):
    i=0
    
    while i<10:
        auxCod=random.randint(100,999)
        pos=busqueda(lc,auxCod)
        if pos==-1:
            lc.append(auxCod)
            lp.append(round(random.uniform(1000,10000),2))
            i+=1
        else:
            print("PRODUCTO DUPLICADO")

def cargaLista(lista):
    
    while len(lista)<10:
        valor=random.randint(100,500)
        pos=busqueda (lista,valor)
        if pos==-1:
            lista.append(valor)

# validar en rango

def validarEnRango(li,ls,cf,texto):
    #li=limite inferior
    #ls=limite superior
    #cf=condicion fin
    #texto= texto o mensaje al usuario
    
    valor=int(input(texto))
    while (valor<li or valor>ls) and valor !=cf:
        valor=int(input(texto))
    return valor

# busqueda

def busqueda(li,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(li):
        if li[i]==valorBuscado:
            pos=i
        i+=1
    return pos

# ordenamiento

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
                
# min max

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