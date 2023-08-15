> integrar laTEX para poder hacer cuentas.
>
> para clase que viene tener hecha la guia 3.
>
>usar thonny o buscar una manera de correr el archivo .py
# estructura secuencial

- ejercicio 2.12  
 #### Una farmacia vende algunos articulos sin descuento y a otros con descuento del 20%. confeccionar un programa que recibiendo el precio original y codigo que indica si es o no con decuento,  informe el precio final (0 no aplica el descuento y 1 aplica el descuento).

 > Pv = precio - descuento x codigo

en el ejemplo es precio = precio - precio * descuento * codigo

- ejercicio 2.9  

entradas:  
numVendedor  
cant  
monto  
salario= 50000  
comision= 5000   
salida:  
salarioFinal

> salarioFinal = salario + 5000 x cant + monto x 0.05

- ejercicio 2.11  
un banco necesita para sus cajeros automaticos un programa que lea una cantidad de dinera e imprima a cauntos billetes equivale, considerando que existen billetes de 1000, 500, 100, 50, 10, 5 y 1.
Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.

entradas:  
monto  
salidas:  
c1000  
c500  
c100  
c50  
c10  
c5  
c1  

> la manera de resolver es haciendo la division de enteros para saber la cantidad y el resto para seguir trabajando con el nro que hay que seguir descomponiendo.
>
>Obigatoriamente tengo que hacer todas las divisiones, para poder imprimir la cantidad de billetes de cada valor que va a devolver.
>
>en el ultimo caso, tengo que imprimir el modulo de 5 ya que esa va  a ser la cantidad de billetes de 1.

## Estructura de decision

Tiene una sola entrada y una sola salida.  
Operadores que se suman: Los que perimten comparar.  

### Operadores de comparacion
- `mayor`: > 
- `menor`: <
-` mayor igual`: >=
- `menor igual`: <=
- `igual`: ==
- `distinto`: !=

### Operadores logicos
permiten hacer mas de una evaluacion sobre la condicion que estamos trantando de controlar.  
- `and` --> se relaciona con la multiplicacion. ambas tienen que ser verdaderas
- `or` --> se realaciona con la suma. con que una sea verdadera alcanza
- `not` --> verdadero 1, falso 0. niega la condicion.

la estrutura de decision se relaciona con el el if en lenguajes de programacion.
```py
if(condicion):
    else:
```
> estar atento a seguir la logica cuando la condicion puede tener salida or el falso y no necesariamente por el verdadero.


*ej 3*

confeccionar un programa que pueda recibir un valor entero y nos informe si es un valor PAR, en caso de no serlo determinar e informar si dicho valor es multiplo de 5.

*ej 4*

confeccionar un programa que ingresando los valores de los tres lados de un triangulo, determine e informe si es equilatero, isoceles o escaleno

equilatero --> tres lados iguales
isoceles --> dos lados iguales
escaleno --> ningun lado igual.

## Lenguaje

- ingreso de datos --> input.
- asignacion de valor/ operaciones --> tilde.
- salida por pantalla --> print.
- no hay inicio ni fin que se traduzca.

python no exige la declaracion de variables.No pide tipo de datos.
Las variables se declaran por valor de iniciacion

La entrada por teclada siempre va a ser tipo texto. Entonces input va a haber que encerrarlo en una funcion:

- valor con enteros int(input("")).
- valor con decimales float(input("")).