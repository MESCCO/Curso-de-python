# Programa para sumar los factoriales de dos números ingresados por el usuario
def obtener_numero():
    while True:
        numero = int(input("Escribe un número positivo: "))
        if numero >= 0:
            return numero
        print("¡Número inválido! Intenta con un número mayor o igual a cero.")

def calcular_factorial(n):
    resultado = 1
    for valor in range(2, n + 1):
        resultado *= valor
    return resultado
#datos
num1 = obtener_numero()
num2 = obtener_numero()
#factoriales
f1 = calcular_factorial(num1)
f2 = calcular_factorial(num2)
# Resultado
total = f1 + f2
print(f"La suma de los factoriales de {num1} y {num2} es: {total}")