import time
import random

def busqueda_binaria(lista, objetivo):
    """
    Función de búsqueda binaria.

    La función recibe una lista ordenada y un objetivo a buscar.
    """
    # Inicializamos los índices izquierdo y derecho para la búsqueda binaria.
    izquierda, derecha = 0, len(lista) - 1

    # Realizamos la búsqueda binaria mientras el índice izquierdo sea menor o igual al índice derecho.
    while izquierda <= derecha:
        # Calculamos el índice medio.
        medio = (izquierda + derecha) // 2

        # Si el elemento en el índice medio es el objetivo, retornamos el índice medio.
        if lista[medio] == objetivo:
            return medio
        # Si el elemento en el índice medio es menor que el objetivo, ajustamos el índice izquierdo.
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        # Si el elemento en el índice medio es mayor que el objetivo, ajustamos el índice derecho.
        else:
            derecha = medio - 1
    # Si no se encuentra el objetivo, retornamos -1.
    return -1

def buscar_elemento(lista):
    """
    Función para buscar un elemento en una lista ordenada.

    Preguntamos al usuario si quiere buscar un elemento en la lista ordenada.
    """
    # Preguntamos al usuario si quiere buscar un elemento en la lista ordenada.
    buscar = input("¿Querés buscar un número en la lista ordenada? (S/N): ").strip().upper()

    # Si el usuario quiere buscar un elemento, comienza el proceso de búsqueda.
    if buscar == "S":

        # Pedimos al usuario que ingrese el número a buscar, ya sea manual o aleatoriamente.
        objetivo_input = input("Ingresá el número que querés buscar (o ENTER para elegir uno aleatorio): ").strip()
        # Si el usuario ingresa un número, lo convertimos a entero. Si no, elegimos uno aleatorio de la lista.
        if objetivo_input.isdigit():
            objetivo = int(objetivo_input)
        else:
            objetivo = random.choice(lista)
        print("Elemento a buscar:", objetivo)

        # Registramos el tiempo de inicio de la búsqueda.
        inicio_busqueda = time.time()

        # Realizamos la búsqueda binaria para encontrar el índice del objetivo en la lista.
        indice = busqueda_binaria(lista, objetivo)

        # Registramos el tiempo de finalización de la búsqueda y calculamos el tiempo total de búsqueda.
        fin_busqueda = time.time()
        tiempo_busqueda = fin_busqueda - inicio_busqueda

        # Determinamos si el elemento fue encontrado o no y mostramos el resultado.
        # Si el índice no es -1 (retorno de busqueda_binaria), significa que el elemento está en la lista.
        if indice != -1:
            resultado = f"Elemento encontrado en la posición {indice}"
        else:
            resultado = "Elemento no encontrado"

        # Mostramos el resultado y el tiempo de búsqueda.
        print(resultado)
        print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")

        # Retornamos el tiempo de búsqueda para su uso posterior.
        return tiempo_busqueda
    # Si la lista no está ordenada, retornamos 0.0 como tiempo de búsqueda.
    else:
        return 0.0