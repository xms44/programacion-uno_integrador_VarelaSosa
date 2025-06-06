import generador
import ordenamiento
import busqueda

def main():
    # Asignamos una variable para controlar el bucle principal del programa.
    bandera = True

    # Iniciamos el bucle principal del programa gracias a `bandera`
    while bandera:
        # Obtenemos la lista original y la mostramos.
        lista_original = generador.obtener_lista()
        print("\nLista original:", lista_original)

        # Ordenamos la lista y medimos el tiempo de ordenamiento, almacenando en nuevas variables el retorno de `ordenar_lista`.
        lista_ordenada, tiempo_ordenamiento, esta_ordenada = ordenamiento.ordenar_lista(lista_original)

        # Permitir buscar en cualquier lista, ordenada o no.
        if esta_ordenada:
            # Si la lista está ordenada, preguntamos al usuario si desea buscar en la lista ordenada.
            lista_para_buscar = lista_ordenada
        else:
            # Si la lista no está ordenada, buscamos directamente en la lista original con búsqueda lineal.
            lista_para_buscar = lista_original

        # Buscamos el elemento elegido o aleatorio y medimos el tiempo de búsqueda.
        tiempo_busqueda = busqueda.buscar_elemento(lista_para_buscar, esta_ordenada)
        ordenamiento.mostrar_resultados(tiempo_ordenamiento, tiempo_busqueda)

        # Preguntamos al usuario si desea realizar otra operación. En caso de que no, bandera pasa a `False` y el bucle termina.
        respuesta = input("\n¿Querés realizar otra operación? (S/N): ").strip().lower()
        if respuesta != 's':
            bandera = False

        print("\nEl programa finalizó.\n")

if __name__ == "__main__":
    main()