"""EN UN NEGOCIO SE CONOCE LA LISTA DE PRECIOS DE 10 PRODUCTOS
Por cada producto conocemos : 
    - EL CODIGO (NRO. ENTERO DE 3 cifras)
    - PRECIO (real)

1) CARGAR LOS DATOS EN LISTAS PARALELAS (CODIGO-PRECIO). ->CARGA
2) MOSTRAR LOS DATOS INGRESADOS -> LISTADO
3) INDICAR LOS PRODUCTOS MAS CAROS -> MAX
4) SE CONSULTA EL PRECIO, SEGUN EL CODIGO DEL PRODUCTO.
5) FIN DE LA CONSULTA CODIGO DE PRODUCTO CERO.
6) Listado ordenado por precio
"""

import random

def busqueda (lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

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

def listado(lc,lp):
    print(" ------- LISTADO DE PRECIOS DE PRODUCTOS -------")
    
    for i in range(len(lc)):
        print(lc[i],"\t",lp[i])

def maximo(lista):
    for i in range(len(lista)):
        if i==0 or lista[i]>valorMax:
            valorMax=lista[i]
    return valorMax

# programa principal
CODIGOS=[]
PRECIOS=[]

cargaInicial(CODIGOS,PRECIOS)
print(CODIGOS)
print(PRECIOS)

listado(CODIGOS,PRECIOS)

precioMaximo=maximo(PRECIOS)

print("\nEl precio maximo es ",precioMaximo)
for i in range(len(CODIGOS)):
    if PRECIOS[i]==precioMaximo:
        print("El codigo de producto mas caro ",CODIGOS[i])
        
print("\n\n CONSULTA DE PRECIOS...")
cod=int(input("Ingrese un codigo - 0 para FINALIZAR "))
while cod!=0:
    pos=busqueda(CODIGOS,cod)
    if pos!=-1:        
        print("El precio del producto $",PRECIOS[pos])
    else:
        print("PRODUCTO INEXISTENTE")
    cod=int(input("Ingrese un codigo - 0 para FINALIZAR "))

              
        
        
        
    








