# TP.3 Estrcturas Condicionles

> *nota*: conditional ternary operator(es6) condition ? true : false

*ej 1:*  
ngresar dos números enteros e indicar si son iguales o distintos  

entrada:  
n1,n2
salida:  
iguales,distintos  
condicioes:  
> n1 = n2 ? iguales : distintos

*ej 2:*  
Leer un número entero e imprimir un mensaje indicando si es par o impar

entrada:  
nEntero
salida:  
par,impar  
condicioes:  

> nEntero ? si : no
>
> si -> n%2 = 0 ? par : impar
>
> no -> "n no es entero"

*ej 3:*  
Desarrollar  un  programa  que  solicite  un  número  de  mes  (por  ejemplo  4)  y
escriba el  nombre  del  mes  en  letras  ("abril").  Verificar  que  el  mes  sea  válido  y
mostrar un mensaje de error en caso de que no lo sea.

entrada:  
nMes
salida:  
mes  
constantes:  
1=enero,2=febrero,3=marzo,4=abril,5=mayo,6=junio,7=julio,8=agosto,9=septiembre,10=octubre,11=noviembre, 12=diciembre.  
condiciones:  

> nMes == 1 ? enero : (nMes == 2 ? febrero : (nMes == 3 ? marzo : (nMes == 4 ? abril : (nMes == 5 ? mayo : (nMes == 6 ? junio : (nMes == 7 ? julio : (nMes == 8 ? agosto : (nMes == 9 ? septiembre : (nMes == 10 ? octubre : (nMes == 11 ? noviembre : (nMes == 12 ? diciembre : "numero invalido")))))))))))

*ej 4:*  
Ingresar  las  notas  de  los  dos  parciales  de  un  alumno  e  indicar  si  promocionó,
aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está
entre 0 y 10.

- Se  promociona  cuando  las  notas  de  ambos  parciales  son  mayores  o
iguales a 7.
- Se aprueba cuando las notas de ambos parciales son mayores o iguales
a 4.
- Se debe recuperar cuando al menos una de las dos notas es menor a 4

entrada:  
n1,n2  
salida:  
prom,aprob,recup,err(nN != 0-10)  
constantes:  
prom = n1 && n2 >= 7,  
aprob = n1 && n2 >= 4,  
recup = n1 || n2 < 4,  
condiciones:  

REVISAR SEGUN HOJA DE EJs
> n1 AND n2 > 10 ?
>
> n1 OR n2 < 4 ? desaprueba : (n1 AND n2 >= 7 ? promociona : aprueba)

*ej 5:*  
Una  editorial  determina  el  precio  de  un  libro  según  la  cantidad  de  páginas  que
contiene. El costo básico del libro es de $500, más $3,20 por página con encuadernación  rústica.  Si  el  número  de  páginas  supera  las  300  la  encuadernación
debe ser en tela, lo que incrementa el costo en $200. Además, si el número de
páginas  sobrepasa  las  600  se  hace  necesario  un  procedimiento  especial  de  encuadernación  que  incrementa  el  costo  en  otros  $336.  Desarrollar  un  programa
que calcule el costo de un libro dado el número de páginas.

*ej 6:*  
Una remisería requiere un programa que calcule el precio de un viaje a partir de
la cantidad de kilómetros que desea recorrer el usuario. Para eso cuenta con la
siguiente tarifa:

- Viaje  mínimo  $250.  Sólo  se  cobra  cuando  el  importe  por  kilómetro  no
alcanza este mínimo.
- Si recorre entre 0 y 10 km: $30 por km
- Si recorre 10 km o más: $20 por km

*ej 7:*  
Leer un número correspondiente a un año e imprimir un mensaje indicando si es
bisiesto o no. Un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos
años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que
también  sean  divisibles  por  400.  Por  ejemplo,  1900  no  fue  bisiesto  pero  sí  el
2000.

*ej 8:*  
Leer  tres  números  correspondientes  al  día,  mes  y  año  de  una  fecha  e  imprimir
un mensaje indicando si la fecha es válida o no.

*ej9:*
