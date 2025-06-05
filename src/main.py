import generador
import ordenamiento
import busqueda

def main():
    # Obtenemos la lista original y la mostramos.
    lista_original = generador.obtener_lista()
    print("\nLista original:", lista_original)

    # Ordenamos la lista y medimos el tiempo de ordenamiento.
    lista_ordenada, tiempo_ordenamiento, esta_ordenada = ordenamiento.ordenar_lista(lista_original)

    # Si la lista está ordenada, se busca un elemento y se mide el tiempo de búsqueda.
    if esta_ordenada:
        tiempo_busqueda = busqueda.buscar_elemento(lista_ordenada)
        ordenamiento.mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda)
    else:
        print("La búsqueda binaria no está habilitada porque no se ordenó la lista.")

    print("\nEl programa finalizó.\n")

if __name__ == "__main__":
    main()