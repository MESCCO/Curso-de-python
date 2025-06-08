#DETERMINAR LA DISTANCIA ENTRE DOS PUNTOS

#COORDENADAS DE A O PRIMER PUNTO

print("Cordenadas del primer punto a")

a_en_eje_x =int(input("En el eje x: "))
a_en_eje_y =int(input("En el eje y: "))

#COORDENADAS DE B O SEGUNDO PUNTO

print("Cordenadas del segundo punto b")

b_en_eje_x =int(input("En el eje x: "))
b_en_eje_y =int(input("En el eje y: "))

#OPERACION

la_distancia_entre_puntos = ((a_en_eje_x - b_en_eje_x)**2 + (a_en_eje_y - b_en_eje_y)**2)**0.5

#RESULTADO

print(f"la distancia entre puntos a y b es:{la_distancia_entre_puntos:.2f}")