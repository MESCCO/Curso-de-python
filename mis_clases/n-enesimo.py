#Escribir un algoritmo que calcule la altura que alcanzará en el n-ésimo rebote

#Datos
altura_inicial = int(input("altura inicial : "))
coeficiente_de_restitucion = float(input("coefieciente de restitucion : "))
numero_de_rebotes = int(input("numero de rebotes : "))
#OPERACION 
altura_en_enesimo_rebote = altura_inicial*((coeficiente_de_restitucion)**(numero_de_rebotes))
print("altura en el eneismo rebote = ",altura_en_enesimo_rebote)