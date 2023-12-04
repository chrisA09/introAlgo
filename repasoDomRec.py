import random



'''
  
extracciones = 1050  --> 10000
tratamiento de conducto = 2035 --> 15000
implantes = 3030 --> 90000
consulta control 9999 --> 5000

'''

codigos = [1050,2035,3030,9999]
valores = [10000,15000,90000,5000]

def validarEnRango(li,ls,cf,texto):
    valor = int(input(texto))
    while (valor<li or valor>ls) and valor != cf:
        valor = int(input(texto))
    return valor
def busqueda(lista,valorBuscado):
    
    pos=-1
    i=0
    while i<len(lista) and pos==-1:
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

# principal

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
    
print(CANTPRA)