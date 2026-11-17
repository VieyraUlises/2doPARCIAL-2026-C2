def ordenar_por_anio_seleccion(canciones):
    n = len(canciones)
    for i in range(n):
        mayor = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[mayor].anio:
                mayor = j
        canciones[i], canciones[mayor] = canciones[mayor], canciones[i]
    return canciones

def ordenar_por_duracion_insercion(canciones):
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones


# Teoria:
# Ambos algoritmos tienen una complejidad de O(n2) en el peor caso, porque realizan comparaciones entre los elementos de la lista mediante recorridos anidados.

# El algoritmo de insercion conserva el orden relativo de las canciones que duran lo mismo, porque solo desplaza elementos
# cuando su duracion es mayor que la del elemento actual. El algoritmo de seleccion no garantiza conservar ese orden relativo,
# porque al intercambiar elementos puede modificar su posicion original.