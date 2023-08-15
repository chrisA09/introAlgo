# TP.2 Estructuras Secuenciales

*ej 2:*  
Desarrollar un programa que permita ingresar dos números enteros A y
B a través del teclado. Imprimir su suma y su diferencia.

entrada:  
a,b  
salida:
suma, resta

>suma = a + b
>
>resta= a - b

*ej 3:*
Calcular el promedio de las notas que obtiene un alumno al rendir los dos
parciales.

entrada:  
n1, n2  
salida:  
promedio

>promedio = (n1 + n2) / 2

*ej 4:*  
Escribir un programa que permita ingresar la edad de una persona en
años y la convierta a días, imprimiendo el resultado. Considerar que todos los años tienen 365 días.

entrada:  
n  
salida:  
nDias  
constante:  
1año = 365dias

> nDias = n x 365

*ej 5:*  
Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.

entrada:  
n1,n2,n3  
salida:  
porcentajeN1,porcentajeN2,porcentajeN3  

>total = n1 + n2 + n3
>
>porcentajeN = (n x 100) / total.

*ej 6:*  
Ingresar tres números enteros, calcular su promedio y mostrarlo por
pantalla.

entrada:  
n1,n2,n3  
salida:  
promedio

>promedio = (n1 + n2 + n3) / 2

*ej 7:*  
Una persona invierte su capital en un banco y desea saber cuánto dinero
ganará en un mes, teniendo en cuenta que el banco paga 2% mensual.
¿Cuánto ganará en seis meses si deja su dinero invertido?

entrada:  
n  
nMeses
salida:  
renta x6  
constantes:  
renta = 0.02

>renta a 6 meses = n x (renta x nMeses)

*ej 8:*  
Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas. Los factores de conversión son:

- 1 pie = 12 pulgadas
- 1 yarda = 3 pies
- 1 pulgada = 2,54 cm.
- 1 metro = 100 cm.

entrada:  
nMetros  
salida:  
nMetros --> cm, pulgadas, pies y yardas  
constantes:  
1 pie = 12 pulgadas
1 yarda = 3 pies
1 pulgada = 2,54 cm.
1 metro = 100 cm.

>`nCm` = nMetros x 100 --> `nPulgadas` = nMetros x (nCm / 2.54) --> `nPies` = nMetrosx (nPulgadas / 12) --> `nYardas` = nMetros x (nPies / 3)

*ej 9:*  
Una inmobiliaria paga a sus vendedores un salario de $50000, más una
comisión de $5000 por cada venta realizada, más el 5% del valor de las
ventas. Realizar un programa que imprima el número del vendedor y el
salario que le corresponde en un determinado mes. Se leen el número
del vendedor, la cantidad de ventas que realizó y el valor total de las
mismas.

entrada:  
nVendedor,
nVentas,
totalVentas,  
salida:  
nVendedor,
salarioTotal  
constantes:  
salario: 50000,
comision: 5000,
bono: 0.05,

> salarioTotal = salario + comision + totalVentas x bono

*ej 10:*  
Leer un período en segundos e imprimirlo expresado en días, horas,
minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días,
7 horas, 33 minutos y 20 segundos.

entrada:  
cantSegundos  
salida:  
nDias,
nHoras,
nMinutos,
nSegundos  
constantes:  
1dia --> 86.4ks,  
1hr --> 3.6ks,  
1min --> 60s,

>equiv = cantSegundos // 1dia, cantSegundos % 1 dia --> equiv // 1hr, equiv % 1hr --> equiv // 60, equiv % 60.

*ej 11:*  
Un banco necesita para sus cajeros automáticos un programa que lea
una cantidad de dinero e imprima a cuántos billetes equivale, considerando que existen billetes de $1000, $500, $100, $50, $10, $5 y $1.
Desarrollar dicho programa de tal forma que se minimice la cantidad de
billetes entregados por el cajero.

*ej 12:*
Escribir un programa para convertir un número binario de 4 cifras en un
número decimal. El número binario se ingresa como un solo número
entero de cuatro dígitos.
Procedimiento: Para convertir un número binario a decimal es necesario
multiplicar el valor de cada dígito por el número 2 elevado a un exponente. Este exponente se obtiene de la posición que ocupa el dígito
dentro del número, comenzando desde la derecha con la posición 0. Todos estos resultados se suman para obtener el valor final. Ejemplo: Convertir 1011 a decimal:

fijarse ejemplo de ecuacion en la guia

entrada:  
n1,n2,n3,n4  
salida:  
nDec  
constantes:  
Para convertir un número binario a decimal es necesario
multiplicar el valor de cada dígito por el número 2 elevado a un exponente. Este exponente se obtiene de la posición que ocupa el dígito
dentro del número, comenzando desde la derecha con la posición 0

> n1 x 2^3 + n2 x 2^2 + n3 x 2^1 + n4 x 2^0 = dec
