#Bucle WHILE
import msvcrt
# -*- coding: utf-8 -*-

#La estructura de while se repite con anio+=1 hasta cumplir la condicion y imprime los resultados
#Podrás notar que en cada iteración, incrementamos el valor de la variable que condiciona
#el bucle (anio). Si no lo hiciéramos, esta variable siempre sería igual a 2001 y el bucle se
#ejecutaría de forma infinita, ya que la condición (anio <= 2012) siempre se estaría
#cumpliendo.

anio = 2001
  while anio <= 2016:
          print "informe del", str(anio)
      if anio == 2016:
          print "Es el 2016!!!"
      if anio == 2004:
          print "Campeones de atenas!!!"
      anio += 1

msvcrt.getch()
