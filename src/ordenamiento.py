import time

"""
Función de ordenamiento Bubble Sort

La función recibe una lista y un parámetro opcional `mostrar_pasos` que por defecto es `False`.
Es `False` para que no muestre los pasos por defecto (depende de ordenar_lista()).
"""

def bubble_sort(lista, mostrar_pasos=False):
    # Obtenemos la longitud de la lista.
    longitud = len(lista)
    # Establecemos un bucle for para iterar sobre la lista.
    # El rango será la longitud de la lista, por más que el ordenamiento se complete antes.
    # Sino deberíamos usar `break` y es mala práctica.
    for pasada in range(longitud):
        # Realizamos las comparaciones y los intercambios necesarios en la lista para ordenarla.
        for i in range(0, longitud - pasada - 1):
            # Comparamos los elementos adyacentes y los intercambiamos si están en el orden incorrecto.
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        # Si el usuario quiere ver los pasos, los mostramos.
        if mostrar_pasos:
            print(f"Iteración {pasada + 1}: {lista}")
    # Retornamos la lista ordenada.
    return lista

def ordenar_lista(lista):
    """
    Función para ordenar una lista usando Bubble Sort.

    Preguntamos al usuario si quiere ordenar la lista.
    """
    respuesta = input("¿Querés ordenar la lista usando Bubble Sort? (S/N): ").strip().upper()
    # Hacemos un retorno temprano o "early return". Si la respuesta no es "S", retornamos la lista original y un tiempo de 0.0.
    # No se ejecutará el resto del código.
    if respuesta != "S":
        return lista[:], 0.0, False
    # Si la respuesta es "S", le preguntamos si quiere ver los pasos del ordenamiento.
    respuesta_pasos = input("¿Mostrar los pasos del ordenamiento? (S/N): ").strip().upper()
    # Inicializamos la variable mostrar_pasos en `False`.
    mostrar_pasos = False
    # Si la respuesta es "S", cambiamos el valor de mostrar_pasos a `True`.
    if respuesta_pasos == "S":
        mostrar_pasos = True

    # Registramos el tiempo de inicio del ordenamiento.
    inicio = time.time()

    # Ordena la lista usando bubble_sort y muestra los pasos si el usuario lo solicitó.
    # `lista[:]` crea una copia de `lista` para no modificar la lista original.
    lista_ordenada = bubble_sort(lista[:], mostrar_pasos=mostrar_pasos)

    # Registramos el tiempo de finalización del ordenamiento.
    fin = time.time()

    # Calculamos el tiempo total de ordenamiento.
    tiempo = fin - inicio

    # Imprimimos la lista ordenada y el tiempo de ordenamiento.
    print("Lista ordenada:", lista_ordenada)
    print(f"Tiempo de ordenamiento: {tiempo:.6f} segundos")

    # Retornamos la lista ordenada, el tiempo de ordenamiento y `True` para indicar que se realizó el ordenamiento.
    return lista_ordenada, tiempo, True

def mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda):
    """
    Función sencilla para mostrar los resultados de los tiempos de ordenamiento y búsqueda.
    """
    print("\nResumen de tiempos:")
    print(f"Tiempo de ordenamiento: {tiempo_ordenamiento:.6f} segundos")
    print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")