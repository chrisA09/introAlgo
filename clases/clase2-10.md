# funciones

- facilita la construccion
- permite absteaer porciones de codigo

> en .py la funcion puede tener varios valores de retorno

las funciones tienen que tener una tarea especifica y debe contener:  

- nombre
- parametros(opcional)
- sentencias que realizan la tarea
- valor que devuelve cuando termina su tarea (opcional).

```py
def nombre (n1,n2): // parentesis obligatorio en la funciones
resu = 0
for i in range(n1):
resu += n2
return resu
```

## Clase 10

Procesar legajos de 4 digitos con funcion ingresaValidaRango, notas de 1-10 con funcion ingresa valida rango. La carga finaliza con legajo 999.

_Informar Nota promedio(funcion calcular y mostrar)
_Procentaje de alumnos con nota < 4 (funcion porcentaje), el informe en el principal """"

### Funcion validar rango - calcularyMostrar

variable = nombreFuncion(limiteInferior, limiteSuperior, "texto")

Esta funcion de validar rango se puede reutilizar en otra variable pudiendo cambiar el contenido tanto de los limites como del texto.

```py
def ingresaValidaRango(li, ls, texto):
    valor=int(input(texto))
    while valor<li or valor>ls:
        valor=int(input(texto))
    return valor
```

```py
def calcularyMostrar(a,b):
    print("el promedio es", a/b)
```

```py
def porcentaje(cg, cp): //contador general, contador particular
    return cp*100/cg
```
