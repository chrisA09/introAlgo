import random

def busqueda (lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def cargaInicial(ll,ln):
    
    auxLegajo=int(input("Ingrese un legajo"))
    while auxLegajo<=0 and auxLegajo !=-1:
        auxLegajo=int(input("Ingrese un legajo"))
    
    while auxLegajo !=-1:
        
        pos=busqueda(ll, auxLegajo)        
        if pos==-1:            
            nota=random.randint(1,10)
            ll.append(auxLegajo)
            ln.append(nota)
        else:
            print("LEGAJO DUPLICADO")
            
        auxLegajo=int(input("Ingrese un legajo"))
        while auxLegajo<=0 and auxLegajo !=-1:
            auxLegajo=int(input("Ingrese un legajo"))
         
            
        
 def ordenamiento (ll,ln):
     
     for i in range(len(ll)-1):
         for j in range(len(ll)-1-i):
             if ll[j]>ll[j+1]:
                 aux=ll[j]
                 ll[j]=ll[j+1]
                 ll[j+1]=aux
                 
                 aux=ln[j]
                 ln[j]=ln[j+1]
                 ln[j+1]=aux
                 
                 
                 
def listado(ll,ln):
    print(" ------- LISTADO DE LEGAJOS Y NOTAS -------")
    
    for i in range(len(lc)):
        print(ll[i],"\t",ln[i])   
        
        



# aqui comienza el principal
LEGAJOS=[]
NOTAS=[]

cargaInicial(LEGAJOS,NOTAS)

print(LEGAJOS)
print(NOTAS)

if len(NOTAS)>0:
    aprobados=0
    desaprobados=0
    suma=0
    
    for i in range(len(NOTAS)):
        
        if NOTAS[i]>=4:
            aprobados+=1
        else:
            desaprobados+=1
        
        suma+=NOTAS[i]
        
    print("La cantidad de aprobados ", aprobados)
    print("La cantidad de desaprobados ",desaprobados)
    
    promedio=suma/len(NOTAS)
    
    print("La nota promedio es ", promedio)
    
    for i in range(len(NOTAS)):
        if NOTAS[i]>promedio:
            print("Legajo que supera el promedio ",LEGAJOS[i])
            
    ordenamiento(LEGAJOS,NOTAS)
    listado(LEGAJOS,NOTAS)
    
else:
    print("NO SE INGRESARON DATOS")
    
    

