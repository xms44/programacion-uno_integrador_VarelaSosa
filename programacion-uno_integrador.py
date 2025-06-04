import random
import time

# Modulos / Funciones

def obtener_lista():
    print("Trabajo Integrador - Programación I")
    entrada = input("¿Cuántos números aleatorios querés generar? (ej: 10): ")
    while not entrada.isdigit():
        print("Por favor, ingresá un número válido.")
        entrada = input("¿Cuántos números aleatorios querés generar? (ej: 10): ")
    cantidad = int(entrada)
    lista = random.sample(range(1, cantidad * 10), cantidad)
    return lista

def bubble_sort(lista, mostrar_pasos=False):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if mostrar_pasos:
            print(f"Iteración {i + 1}: {lista}")
    return lista

def ordenar_lista(lista):
    opcion = input("¿Querés ordenar la lista usando Bubble Sort? (S/N): ").strip().upper()
    if opcion == "S":
        mostrar_pasos_input = input("¿Mostrar los pasos del ordenamiento? (S/N): ").strip().upper()
        mostrar_pasos = mostrar_pasos_input == "S"

        inicio = time.time()
        lista_ordenada = bubble_sort(lista[:], mostrar_pasos=mostrar_pasos)
        fin = time.time()
        tiempo = fin - inicio

        print("Lista ordenada:", lista_ordenada)
        print(f"Tiempo de ordenamiento: {tiempo:.6f} segundos")
        return lista_ordenada, tiempo, True
    else:
        return lista[:], 0.0, False

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def buscar_elemento(lista):
    buscar = input("¿Querés buscar un número en la lista ordenada? (S/N): ").strip().upper()
    if buscar == "S":
        objetivo_input = input("Ingresá el número que querés buscar (o ENTER para elegir uno aleatorio): ").strip()
        if objetivo_input.isdigit():
            objetivo = int(objetivo_input)
        else:
            objetivo = random.choice(lista)
        print("Elemento a buscar:", objetivo)

        inicio_busqueda = time.time()
        indice = busqueda_binaria(lista, objetivo)
        fin_busqueda = time.time()
        tiempo_busqueda = fin_busqueda - inicio_busqueda
        
        if indice != -1:
            resultado = f"Elemento encontrado en la posición {indice}"
        else:
            resultado = "Elemento no encontrado"
        print(resultado)
        print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")
        return tiempo_busqueda
    else:
        return 0.0

def mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda):
    print("\nResumen de tiempos:")
    print(f"Tiempo de ordenamiento: {tiempo_ordenamiento:.6f} segundos")
    print(f"Tiempo de búsqueda: {tiempo_busqueda:.6f} segundos")

# Programa principal

def main():
    lista = obtener_lista()
    print("\nLista original:", lista)

    lista_ordenada, tiempo_ordenamiento, ordenada = ordenar_lista(lista)

    if ordenada:
        tiempo_busqueda = buscar_elemento(lista_ordenada)
        mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda)
    else:
        print("La búsqueda binaria no está habilitada porque no se ordenó la lista.")

if __name__ == "__main__":
    main()