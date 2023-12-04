import random


def busqueda(lista, valorBuscado):
    pos = -1
    i = 0
    while pos==-1 and i < len(lista):
        if lista[i] == valorBuscado:
            pos = i
        i += 1
    return pos

def cargaInicial(lista):
    while len(lista) < 10:
        valor = random.randint(100,500)
        pos = busqueda(lista, valor)
        if pos == -1:
            lista.append(valor)
        
def cargaMediciones():
    lista = []
    for i in range (10):
        lista.append(random.randint(0,200))
    return lista
        
def mostarDatos(lista1, lista2):
    
    print("\t","MEDICIONES LLUVIAS CAIDAS")
    print("ESTACION","\t","mm CAIDOS")
    
    for i in range(len(lista1)):
        print(lista1[i],"\t","\t",lista2[i])

def minimo(lista):
    pos = 0 
    for i in range(len(lista)):
        if i == 0 or lista[i] < valorMinimo:
            valorMinimo = lista[i]
            pos = i
    return (pos)

def maximo(lista):
    pos = 0 
    for i in range(len(lista)):
        if i == 0 or lista[i] > valorMaximo:
            valorMaximo = lista[i]
            pos = i
    return (pos)

def ordenamiento (lista1, lista2):
    for i in range(len(lista1)-1):
        for j in range(len(lista1)-1-i):
            if lista1[j] > lista1[j+1]:
                aux = lista1[j]
                lista1[j] = lista1[j+1]
                lista1[j+1] = aux
                
                aux = lista2[j]
                lista2[j] = lista2[j+1]
                lista2[j+1] = aux

# programa principal

'''
1) 
'''
estaciones = []
cargaInicial(estaciones)
print(estaciones)

'''
2)
'''

mediciones = cargaMediciones()
print(mediciones)

'''
3)
'''

mostarDatos(estaciones, mediciones)

'''
4)
'''

minPos = minimo(mediciones)
maxPos = maximo(mediciones)
print("valor minimo: ",mediciones[minPos],"\t","estacion: ",estaciones[minPos])
print("valor maximo: ",mediciones[maxPos],"\t","estacion: ",estaciones[maxPos])

'''
5)
'''

ordenamiento(estaciones,mediciones)
mostarDatos(estaciones,mediciones)

'''
7)
'''

consultaValor = int(input("ingrese valor de lluvia caida de 0 a 200"))
consulta = busqueda(mediciones,consultaValor)

if consulta != -1:
    
    print("valor encontrado, medido por estacion: ",estaciones[consulta])
    
else:
    
    print("no se encontro tal valor")