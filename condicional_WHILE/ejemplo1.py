#Bucle WHILE
import msvcrt
# -*- coding: utf-8 -*-

#La estructura de while se repite con anio+=1 hasta cumplir la condicion y imprime los resultados

anio = 2001
  while anio <= 2016:
          print "informe del", str(anio)
      if anio == 2016:
          print "Es el 2016!!!"
      if anio == 2004:
          print "Campeones de atenas!!!"
      anio += 1

msvcrt.getch()
