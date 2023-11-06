'''
- EXTRACCIONES (CODIGO=1050) --> $10000 
- TRATAMIENTO DE CONDUCTO (CODIGO =2035) --> 15000 
- IMPLANTES (CODIGO=3030)  --> 90000
- CONSULTA DE CONTROL (CODIGO =9999) --> 5000

'''

def test (dni, codigo, edad):


    '''
    - los datos del enunciado los dispone como listas para arrancar a hacer el ejercicio
    si el array es vacio, no importa

    - trabja de manera inteligente, usando los valores de los array para mutliplicar y sacer el valor de cada practica teniendo los datos ahi
    
    - tener en cuenta el orden de los array que se vinculan y los array en general OJO! EL ORDEN DE LOS ARRAYS/LISTAS!!!

    - tratar de usar siempre que se pueda, arrays, nada de hardcodeo. 

    - usa una lista como contador para cuando sabe de antemano el length

    - los arrays que creo dentro de una funcion los tengo que devolver, si lo inicialize antes no hace falta
    
    - Importante el uso de las vinculaciones entre arrays para la devolucion de valores

    - REQUERIMIENTO! la busqueda tiene que ser SIEMPRE con 'WHILE', nunca con 'FOR'. "Nadie sigue buscando cuando encuentra algo"
    
    - se puede usar cualquier algoritmo de ordenamiento

    - IMPRESINDIBLE FUNCION DE BUSQUEDA
    '''
    dniInvalido = []
    codInvalido = []
    
    total = 0
    totalExtraccion = 0
    totalConducto = 0
    totalImplantes = 0
    totalConsulta = 0


    #CANTIDAD TIENE QUE IR EN UN ARRAY Y SORT DE MENOR A MAYOR
    cantExtraccion = 0
    cantConducto = 0
    cantImplantes = 0
    cantConsulta = 0
    
    edad = 0
    
    # validar rango dni y guardar dni invalido en array
    
    def validarEnRango (a,b,c):
        dni = int(input('ingrese dni'))
        while (dni < a or dni > b) and dni != c:
	        dni = int(input('ingrese dni'))
    return dni
 
        
    while( dni != -1):
        #Ingreso codigo
        if codigo != 1050 and codigo != 1050 and codigo != 1050 and codigo != 1050:
            
            # hace falta guardar en un array dni y codigo de practica rechazado

            codInvalido.append(codigo)
            # print(f'codigo {codigo} no valido')
        # Ingreso edad


print(test)

'''
DNI=int(input("ingrese un correcto valor de dni: "))
	    
        while (DNI < 10000000 or DNI > 99999999) and DNI!= -1:
		    DNI=int(input("ingrese un correcto valor de dni: "))
    return DNI
'''
