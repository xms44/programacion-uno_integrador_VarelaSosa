import random

def obtener_lista():
    # Imprimimos un mensaje de bienvenida al usuario
    print("\nTrabajo Integrador - Programación I\n")
    # Solicitamos al usuario que ingrese la cantidad de números aleatorios que busca generar
    entrada = input("¿Cuántos números aleatorios querés generar? (ej: 10): ")
    # Validamos que la entrada sea un número entero
    while not entrada.isdigit():
        print("Por favor, ingresá un número válido.")
        entrada = input("¿Cuántos números aleatorios querés generar? (ej: 10): ")
    # Convertimos la entrada a un número entero
    cantidad = int(entrada)
    # Generamos una lista de números aleatorios
    lista = random.sample(range(1, cantidad * 10), cantidad)
    # Retornamos la lista generada
    return lista