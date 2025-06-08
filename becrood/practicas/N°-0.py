
# Cuerpo del programa
n_1 = int(input('Introduzca el n 1: '))
n_2 = int(input('Introduzca el n 2: '))

suma_x = 0
suma_y = 0

for i in range(1, n_1):  # hasta n_1 - 1
    if n_1 % i == 0:
        suma_x += i

for k in range(1, n_2):  # hasta n_2 - 1
    if n_2 % k == 0:
        suma_y += k

if suma_x ==n_2 and suma_y==n_1 :
    print('¡Son amigos! :)')
else:
    print('No son amigos :(')