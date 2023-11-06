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

# utility

# validar rango

def validarEnRango(li,ls,cf,texto):
    valor = int(input(texto))
    while (valor<li or valor>ls) and valor != cf:
        valor = int(input(texto))
    return valor

print(validarEnRango(10,100,-1,"ingrese valor"))


