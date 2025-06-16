# Validar si el usuario y la contraseña tienen mínimo 8 caracteres

def revisar_datos(nombre, clave):
    if len(nombre) >= 8 and len(clave) >= 8:
        return "Todo bien, válido"
    else:
        return "El usuario o la contraseña deben tener al menos 8 caracteres"

def ejercicio_validacion():
    nombre = input("Ingresa tu nombre de usuario: ")
    clave = input("Ingresa tu contraseña: ")
    resultado = revisar_datos(nombre, clave)
    print(resultado)

# Menú básico para elegir una opción

def mostrar_menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Validar usuario y contraseña")
        print("2. Salir")

        opcion = input("Elige una opción (1-2): ")
        if opcion == "1":
            ejercicio_validacion()
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta otra vez.")
mostrar_menu()