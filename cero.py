import random

def validarEnRango(li,ls,cf, texto):
    
    valor = int(input(texto))
    
    while (valor < li or valor > ls) and valor != cf:
        
        valor = int(input(texto))
    return valor
    
def busqueda( lista , valorBuscado):
    pos = -1
    i = 0
    while i < len(lista) and pos == -1:
        if lista[i] == valorBuscado:
            pos = i
        i += 1
    return pos

def ordenamiento(lista1, lista2, lista3):
    for i in range(len(lista1)-1):
        for j in range(len(lista1)-1-i):
            if lista1[j]>lista1[j+1]:
                aux = lista1[j]
                lista1[j]=lista1[j+1]
                lista1[j+1]= aux
                
                aux = lista2[j]
                lista2[j]=lista2[j+1]
                lista2[j+1]= aux
                
                aux = lista3[j]
                lista3[j]=lista3[j+1]
                lista3[j+1]= aux
    

# principal

cantPracticas = [0]*4
practicas = [1050,2035,3030,9999]
costo = [10000, 15000, 90000, 5000]

dni = []
rechazadas = []

band = 0    # usa la bandera para inicializar edadMinima
i = 0   # usa i como contador de ingreso de datos

auxDni = validarEnRango(10000000,99999999, -1, "ingresar dni --> ")

while auxDni != -1:
    
    auxEdad = int(input("ingresar edad -->"))
    
    if auxEdad > 21:
        
        i += 1
        auxPractica = int(input("ingrese un codigo de practica -- 1050, 2035 ,3030, 9999 --> "))
        
        '''
        Busqueda lo utiliza para saber si se ingreso o no una practica valida
        si devuelve -1 no se econtro practica valida, entonces, va a guadra en su lista correspondiente dni y practica rechazada
        '''
        auxValidacion = busqueda(practicas, auxPractica)
        
        if auxValidacion == -1:
            dni.append(auxDni)
            rechazadas.append(auxPractica)
            print("practica rechazada")
        else:
            cantPracticas[auxValidacion] += 1
            
            if auxPractica == 3030:
                if band == 0 or edadMinima > auxEdad:
                    edadMinima = auxEdad
                    band = 1
    else:
        print ("no se puede atender a menores de 21 años")
    
    auxDni = validarEnRango(10000000,99999999, -1, "ingresar dni --> ")
    
if i > 0: 
    '''
    a- lista de dni - practicas reachazadas
    '''
    print("rechazados")
    for i in range(len(rechazadas)):
        print (dni[i], "\t", rechazadas[i])
        
    '''
    b- total recaudado por practica y total general
    '''
    print("recaudacion por practica")
    suma = 0
    for i in range (len(practicas)):
        suma += cantPracticas[i] * costo[i]
        print(practicas[i], "\t", cantPracticas[i] * costo[i])
    print("recaudacion total", "\t", suma)
    
    '''
    c- mostar cantidad de prácticas de cada tipo que se atendieron ordenadas por cantidad de atendidos
    en forma ascendente
    '''
    
    print("cantidad de prácticas de cada tipo que se atendieron ordenadas por cantidad de atendidos")
    ordenamiento(practicas,costo,cantPracticas)
    
    for i in range(len(practicas)):
        print("practica",practicas[i],"\t","cantidad",cantPracticas[i])
        
    '''
    d- edad del paciente más joven que se realizaron implantes
    '''
    print("edad del paciente más joven que se realizaron implantes","\t",edadMinima)