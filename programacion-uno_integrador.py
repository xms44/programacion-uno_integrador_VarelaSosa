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

# Función para realizar la búsqueda binaria en una lista ordenada.
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

# Función para realizar la búsqueda lineal en una lista, tanto ordenada como desordenada.
def busqueda_lineal(lista, objetivo):
    # Recorremos la lista y comparamos cada elemento con el objetivo.
    for i, valor in enumerate(lista):
        # Si encontramos el objetivo, retornamos su índice.
        if valor == objetivo:
            return i
    # Si no se encuentra el objetivo, retornamos -1.
    return -1


def buscar_elemento(lista, ordenada):
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

        # Brindamos al usuario la posibilidad de elegir el método de búsqueda..
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


# Función sencilla  para mostrar los resultados de los tiempos de ordenamiento y búsqueda.
def mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda):
    print("\nResumen de tiempos:")
    print(f"Tiempo de ordenamiento: {tiempo_ordenamiento:.6f} segundos")
    print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")

# Programa principal

def main():
    
    # Asignamos una variable para controlar el bucle principal del programa.
    bandera = True

    # Iniciamos el bucle principal del programa gracias a `bandera`
    while bandera:
        # Obtenemos la lista original y la mostramos.
        lista_original = obtener_lista()
        print("\nLista original:", lista_original)

        # Ordenamos la lista y medimos el tiempo de ordenamiento, almacenando en nuevas variables el retorno de `ordenar_lista`.
        lista_ordenada, tiempo_ordenamiento, esta_ordenada = ordenar_lista(lista_original)

        # Permitir buscar en cualquier lista, ordenada o no.
        if esta_ordenada:
            # Si la lista está ordenada, preguntamos al usuario si desea buscar en la lista ordenada.
            lista_para_buscar = lista_ordenada
        else:
            # Si la lista no está ordenada, buscamos directamente en la lista original con búsqueda lineal.
            lista_para_buscar = lista_original

        # Buscamos el elemento elegido o aleatorio y medimos el tiempo de búsqueda.
        tiempo_busqueda = buscar_elemento(lista_para_buscar, esta_ordenada)
        mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda)

        # Preguntamos al usuario si desea realizar otra operación. En caso de que no, bandera pasa a `False` y el bucle termina.

        respuesta = input("\n¿Querés realizar otra operación? (S/N): ").strip().lower()
        if respuesta != 's':
            bandera=False
        
        print("\nEl programa finalizó.\n")

if __name__ == "__main__":
    main()