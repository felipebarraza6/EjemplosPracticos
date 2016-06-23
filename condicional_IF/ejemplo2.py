import msvcrt
#Ejemplo if anidados si gasto hasta 100 mil pago con efectivo, si gasto mas de 100 pero menos de 300 pago con debito pero! 
#si gasto mas de 300 pago con credito.

compra = 500

if compra <= 100:
    print 'pago en efectivo'
elif compra > 100 and compra < 300:
      #el "and" es un operador logico y asi decimos que se deben cumpliar ambas condiciones para 
      #imprimir "pago con debito".
    print 'pago con tarjeta de debito'
else:
    print 'Pago con tarjeta de credito'

msvcrt.getch()
