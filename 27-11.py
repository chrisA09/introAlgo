import random
def busqueda (li,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(li):
        if li[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def cargaLista(li):
    i=0
    
    while i<10:
        auxCod=random.randint(100,500)
        pos=busqueda(li,auxCod)
        if pos==-1:
          li.append(auxCod)
            
          i+=1
        else:
          print("CODIGO DUPLICADO")
def cargaMediciones(li):
    i=0
    
    while i<10:
        auxCod=random.randint(0,200)
        pos=busqueda(li,auxCod)
        if pos==-1:
          li.append(auxCod)
            
          i+=1
    
def MostrarDatos(li1,li2):
    for i in range(len(li1)):
        print('estacion',li1[i],'\t','mediciones mm',li2[i])
    
def minMax(list):
    j=0
    for j in range(len(listaMm)):
       if j==0 or list[j] < minimo:
            minimo=list[j]
            
       if j==0 or list[j]>maximo:
            maximo=list[j]
            
    print("minimo:", minimo,"maximo:", maximo)
  
def ordenamiento ():

    for i in range(0,len(lista1)-1):
        for j in range(0,len(lista1)-1-i)
                


licodigos=[]
listaMm=[]
cargaLista(licodigos)
cargaMediciones(listaMm)
MostrarDatos(licodigos,listaMm)
minMax(listaMm)
