import msvcrt

#En los ejemplos anteriores, nombre y color, son dos variables declaradas en tiempo de
#ejecución (es decir, se declaran dinámicamente durante el bucle), asumiendo como valor,
#el de cada elemento de la lista (o tupla) en cada iteración.

#por cada ano en el rango 2001  a 20013 imprimir frase
for anio in range(2001, 2013):
    print "Informes de ", str(anio)
    
msvcrt.getch()
