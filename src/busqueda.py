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

def busqueda_lineal(lista, objetivo):
    """
    Función de búsqueda lineal.

    La función recibe una lista y un objetivo a buscar.
    """
    # Recorremos la lista y comparamos cada elemento con el objetivo.
    for i, valor in enumerate(lista):
        # Si encontramos el objetivo, retornamos su índice.
        if valor == objetivo:
            return i
    # Si no se encuentra el objetivo, retornamos -1.
    return -1

def buscar_elemento(lista, ordenada):
    """
    Función para buscar un elemento en una lista.

    Preguntamos al usuario si quiere buscar un elemento en la lista.
    """
    # Preguntamos al usuario si quiere buscar un elemento en la lista.
    buscar = input("¿Querés buscar un número en la lista? (S/N): ").strip().upper()

    if buscar == "S":
        # Brindamos al usuario la posibilidad de elegir el número a buscar.
        objetivo_input = input("Ingresá el número que querés buscar (o ENTER para elegir uno aleatorio): ").strip()
        if objetivo_input.isdigit():
            objetivo = int(objetivo_input)
        else:
            objetivo = random.choice(lista)
        print("Elemento a buscar:", objetivo)

        # Brindamos al usuario la posibilidad de elegir el método de búsqueda.
        if ordenada:
            tipo_busqueda = input("¿Qué tipo de búsqueda querés usar? (B)inaria / (L)ineal: ").strip().upper()
        else:
            # Si la lista no está ordenada, forzamos la búsqueda lineal.
            print("\nLa lista no está ordenada. Se usará búsqueda lineal.\n")
            tipo_busqueda = "L"

        # Iniciamos la medición del tiempo de búsqueda.
        inicio_busqueda = time.time()

        if tipo_busqueda == "B":
            indice = busqueda_binaria(lista, objetivo)
        else:
            indice = busqueda_lineal(lista, objetivo)

        # Finalizamos la medición del tiempo de búsqueda.
        fin_busqueda = time.time()
        tiempo_busqueda = fin_busqueda - inicio_busqueda

        # Damos los resultados de la búsqueda.
        if indice != -1:
            resultado = f"Elemento encontrado en la posición {indice}"
        else:
            resultado = "Elemento no encontrado"

        print(resultado)
        print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")
        return tiempo_busqueda
    else:
        # Retornamos 0 si la lista está vacía.
        return 0.0