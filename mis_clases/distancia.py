#DETERMINE LA DISTANCIA ENTRE LA TORTUGA Y LA LIEBRE
print("determinando la distancia entre la tortuga y la liebre ")

#DATOS 
velocidad_liebre = 400 #metros/minuto
velocidad_tortuga = 0.6 #metros/minuto

#VELOCIDAD EN METROS POR SEGUNDO

velocidad_liebre_segundos = velocidad_liebre / 60 #metros/segundo
velocidad_tortuga_segundos = velocidad_tortuga / 60 #metros/segundo
 
#TIEMPO

tiempo = int(input("tiempo transcurrido = ")) #en segundos
 
#DISTANCIA EN EL N-SEGUNDO CON RESPECTO AL ORIGEN
distancia_liebre = velocidad_liebre_segundos * tiempo
distancia_tortuga = velocidad_tortuga_segundos * tiempo

#DISTANCIA ENTRE  LIEBRE Y TORTUGA 

distancia = ((distancia_liebre)**2 + + (distancia_tortuga)**2 )**0.5

# RESULTADO 

print("la distancia entre libre y tortuga es = ",distancia)