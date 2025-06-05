import random
import time

# Modulos / Funciones

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

""" Función de ordenamiento Bubble Sort

La función recibe una lista y un parámetro opcional `mostrar_pasos` que por defecto es `False`. Es `False` para que no muestre los pasos por defecto (depende de ordenar_lista()). """

def bubble_sort(lista, mostrar_pasos=False):
    # Obtenemos la longitud de la lista.
    longitud = len(lista)
    # Establecemos un bucle for para iterar sobre la lista. 
    # El rango será la longitud de la lista, por más que el ordenamiento se complete antes. Sino deberíamos usar `break` y es mala práctica.
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
    # Preguntamos al usuario si quiere ordenar la lista.
    respuesta = input("¿Querés ordenar la lista usando Bubble Sort? (S/N): ").strip().upper()
    # Hacemos un retorno temprano o "early return". Si la respuesta no es "S", retornamos la lista original y un tiempo de 0.0. No se ejecutará el resto del código.
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

    # Ordena la lista usando bubble_sort y muestra los pasos si el usuario lo solicitó. `lista[:]` crea una copia de `lista` para no modificar la lista original.

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


def busqueda_binaria(lista, objetivo):
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

# Función sencilla  para mostrar los resultados de los tiempos de ordenamiento y búsqueda.
def mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda):
    print("\nResumen de tiempos:")
    print(f"Tiempo de ordenamiento: {tiempo_ordenamiento:.6f} segundos")
    print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")

# Programa principal

def main():
    
    # Obtenemos la lista original y la mostramos.
    lista_original = obtener_lista()
    print("\nLista original:", lista_original)

    # Ordenamos la lista y medimos el tiempo de ordenamiento, almacenando en nuevas variables el retorno de `ordenar_lista`.
    lista_ordenada, tiempo_ordenamiento, esta_ordenada = ordenar_lista(lista_original)

    # Si la lista está ordenada, se busca un elemento y se mide el tiempo de búsqueda.
    if esta_ordenada:
        tiempo_busqueda = buscar_elemento(lista_ordenada)
        mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda)
    # Si no está ordenada, mostramos un mensaje indicando que no se puede realizar la búsqueda binaria.
    # Caso de "early return" en la función `ordenar_lista`.
    else:
        print("La búsqueda binaria no está habilitada porque no se ordenó la lista.")
    
    print("\nEl programa finalizó.\n")

if __name__ == "__main__":
    main()