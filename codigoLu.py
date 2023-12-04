def ValidarEnRango(li,ls,nf,texto):
    auxCod=int(input(texto))
    while (auxCod<li or auxCod>ls) and auxCod !=nf:
            auxCod=int(input(texto))

    return auxCod
def busqueda(li,valorBuscado):
    pos=-1
    i=0
    while pos ==-1 and i<len(li):
        if li[i]==valorBuscado:
            pos=i
        i+=1
    return pos
def ordenamiento(lista1, lista2,lista3):
    for i in range(len(lista1)-1):
        for j in range(len(lista1)-1-i):
            if lista1[j]>lista1[j+1]:
                aux=lista1[j]
                lista1[j]=lista1[j+1]
                lista1[j+1]=aux
                
                aux=lista2[j]
                lista2[j]=lista2[j+1]
                lista2[j+1]=aux
                
                aux=lista3[j]
                lista3[j]=lista3[j+1]
                lista3[j+1]=aux


#programaprincipal

CODIGOS=[1050,2035,3030,9999]
COSTOS=[1000,15000,90000,5000]
CANTPRA=[0]*4
contador=0
band=0
DNIR=[]
PRAR=[]

DNI= ValidarEnRango(10000000, 99999999, -1, 'ingrese su DNI: ')

while DNI != -1:
    edad=int(input('ingrese su edad'))
    if edad >21:
        contador+=1
        codigo=int(input('ingrese codigo de practica'))
        pos=busqueda(CODIGOS,codigo)
        if pos == -1:
            print('practica rechazada')
            DNIR.append(DNI)
            PRAR.append(codigo)
        else:
            CANTPRA[pos]+=1
            
            if codigo ==3030:
                if band == 0 or edadMini<edad:
                    edadMini=edad
                    band=1
                    
                
    else:
        print('no tiene la edad suficiente')
    DNI= ValidarEnRango(10000000, 99999999, -1, 'ingrese su DNI: ')
    
    
if contador > 0:    
    for i in range(len(DNIR)):
        print('\n', 'practicas rechazadas')
        print('\t', DNIR[i], '\t', PRAR[i])
    suma=0
    for i in range(len(CANTPRA)):
        suma+=CANTPRA[i]*COSTOS[i]
        print('cantidad recaudada por codigo',CANTPRA[i]*COSTOS[i])
    print('la suma de todo es',suma)   
else:
    print('no se ingresaron datos')