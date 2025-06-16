#VENTA DE LIEBRES 

#ENTRADA DE DATOS 

print("Informacion sobre la venta de liebres")

total_de_liebres = int(input("Cantidad de liebres vendidas : "))
costo_por_liebre = int(input("precio de cada liebre : "))

#CALCULOS 

impuesto_unitario = costo_por_liebre * 0.18 #(igv=18%)
impuesto_total = costo_por_liebre * 0.18 * total_de_liebres

valor_de_venta_unitario = impuesto_unitario + costo_por_liebre 
valor_de_venta_total = impuesto_total + costo_por_liebre * total_de_liebres

importe_total = valor_de_venta_unitario * total_de_liebres

#RESULTADO

print("Impuesto unitario = ",impuesto_unitario)
print("Impuesto total = ",impuesto_total)
print("Valor de venta unitario = ",valor_de_venta_unitario)
print("Valor de venta total = ",valor_de_venta_total)
print("Importe total = ",importe_total)