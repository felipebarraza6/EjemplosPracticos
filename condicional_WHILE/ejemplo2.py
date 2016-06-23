import msvcrt
# -*- coding: utf-8 -*-
#Pero que pasa si el valor no es un numero y no puede incrementarse, en ese caso podemos utilizar una estructura de control
#condicional anidada dentro de un bucle y frenar la ejecucion cuando el condicionar deje de cumplirse con la palabra reservada
#break

while True:
    nombre = raw_input("Indique su nombre: ")
    if nombre:
        print "tu nombre es",nombre
        print "Adios!!! presiona enter"
        break
    else:   
        print "debes introducir un nombre"
        

msvcrt.getch()
