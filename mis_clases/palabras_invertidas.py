# Escribir un programa que pida una frase al usuario y la escriba invirtiendo las letras de la frase
frase = input("Ingresa la frase: ")
palabras = frase.split(" ")
palabras_invertidas = []

for palabra in palabras:
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    palabras_invertidas.append(palabra_invertida)

frase_final = " ".join(palabras_invertidas)
print("La frase invertida es:", frase_final)