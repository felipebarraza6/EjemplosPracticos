import msvcrt
#Si la compra es mayor a $100, obtenga un descuento del 10%
total_compra = 120
importe_a_pagar = total_compra
#Como en otros lenguajes podemos llegar el valor de una varibale a otra variable esta es una buena practica para el encapsulamiento de datos

if total_compra > 100:
    tasa_descuento = 10
    importe_descuento = total_compra * tasa_descuento / 100
    importe_a_pagar = total_compra - importe_descuento
    
    print 'Descuento adquirido! debes pagar: ', str(importe_a_pagar)
    
msvcrt.getch()
