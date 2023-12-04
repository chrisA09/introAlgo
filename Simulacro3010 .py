"""
Un consultorio odontológico que atiene únicamente en forma PARTICULAR trabaja con cuatro tipos de prácticas:

-EXTRACCIONES (CODIGO=1050)
-TRATAMIENTO DE CONDUCTO (CODIGO =2035)
-IMPLANTES (CODIGO=3030)
-CONSULTA DE CONTROL (CODIGO =9999)

Cada practica tiene un costo que el paciente abona:
EXTRACCIONES $10000, TRATAMIENTO DE CONDUCTO $15000, IMPLANTES $90000, CONSULTA DE CONTROL $5000

Cada vez que un paciente se atiende se ingresa:
• DNI (Valor entre 10000000 y 99999999) - UTILIZAR FUNCION validarEnRango QUE VALIDE EL INGRESO DE ESTE DATO
• Código de práctica. (entero de 4 digitos)
• Edad del paciente (únicamente mayores a 21 años)

El registro de las atenciones finaliza con un DNI de paciente igual a -1.
Si algún paciente refiere una practica que no se ofrece indicar un error, se deberán guardar e informar al finalizar el listado de practicas rechazadas y a que DNI las solicito.
a- (20%) Listado de pacientes con practicas rechazadas
LISTADO PACIENTES PRACTICAS RECHAZADAS
DNI     COD PRACTICA
XXXXXXX XXXX
XXXXXXX XXXX
XXXXXXX XXXX
… ….
b- (20%) Informar el total recaudado por practica y el total general.
c- (20%) Informar la cantidad de prácticas de cada tipo que se atendieron ordenadas por cantidad de atendidos
en forma ascendente.
d- (20%) Informar la edad del paciente más joven que se realizaron implantes.
    
    
COMPRENSION DEL ENUNCIADO y BUENAS PRACTICAS DE PROGRAMACION SUMAN 20% adicional
"""


def validarEnRango(li,ls,cf,texto):
    #li=limite inferior
    #ls=limite superior
    #cf=condicion fin
    #texto= texto o mensaje al usuario
    
    valor=int(input(texto))
    while (valor<li or valor>ls) and valor !=cf:
        valor=int(input(texto))
    return valor

def busqueda(lista,valorBuscado):
    
    pos=-1
    i=0
    while i<len(lista) and pos==-1:
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

def ordenamiento (lista1,lista2,lista3):
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

#aqui comienza el programa principal
CANTPRA=[0]*4
IMPORTES=[10000,15000,90000,5000]
PRACTICAS=[1050,2035,3030,9999]
dniR=[]
praR=[]

band=0
i=0

auxDni=validarEnRango(10000000,99999999,-1,"Ingrese un dni -> ")

while auxDni!=-1:
     
    auxEdad=int(input("Ingrese una edad mayor a 21 -> "))
    
    if auxEdad>21:
        i+=1
        auxPrac=int(input("Ingrese una practica -> 1050,2035,3030,9999 "))
        
        posicion=busqueda(PRACTICAS,auxPrac)
        
        if posicion ==-1:
            dniR.append(auxDni)
            praR.append(auxPrac)
            print("PRACTICA RECHAZADA!")
        else:
            CANTPRA[posicion]+=1
            
            if auxPrac==3030:
                if band==0 or edadMinI<auxEdad:
                    edadMinI=auxEdad
                    band=1
            
    else:
        print("No se puede atender por ser menor a 21 años!")
    
    auxDni=validarEnRango(10000000,99999999,-1,"Ingrese un dni ")
   
   
if i>0:
    
    """
    a- (20%) Listado de pacientes con practicas rechazadas
    LISTADO PACIENTES RECHAZADOS
    DNI     COD PRACTICA
    XXXXXXX XXXX
    XXXXXXX XXXX
    XXXXXXX XXXX"""
    print("\n\n     LISTADO PACIENTES RECHAZADOS")
    print("\tDNI          COD PRACTICA")
    
    for i in range(len(dniR)):
        print("\t",dniR[i],"\t",praR[i])
    
    
    """
    b- (20%) Informar el total recaudado por practica y el total general.
    """
    suma=0
    print("\n\nRECAUDACION POR PRACTICA")
    for i in range(len(PRACTICAS)):
        suma+=CANTPRA[i]*IMPORTES[i]
        print("\t",PRACTICAS[i],"\t",CANTPRA[i]*IMPORTES[i])
    print("TOTAL RECAUDADO ", suma)

    """
    c- (20%) Informar la cantidad de prácticas de cada tipo que se atendieron
    ordenadas por cantidad de atendidos.
    """
    ordenamiento(CANTPRA,PRACTICAS,IMPORTES)
    
    print("\n\nCANTIDAD DE ATENCIONES POR PRACTICA")
    for i in range(len(PRACTICAS)):    
        print("\t",PRACTICAS[i],"\t",CANTPRA[i])

    
    """
    d- (20%) Informar la edad del paciente más joven que se realizaron implantes.
   """
    print("\n\nLa edad del paciente mas joven que se hizo un implante es ",edadMinI)
    
    
else:
    print("NO SE INGRESARON DATOS!")
    
                
            

            
            
    
    
    
    
    