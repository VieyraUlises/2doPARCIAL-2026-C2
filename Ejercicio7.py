def busqueda_lineal(canciones, campo, valor):
    resultado = []
    for cancion in canciones:
        if campo == "titulo":
            if cancion.titulo == valor:
                resultado.append(cancion)
        elif campo == "artista":
            if cancion.artista == valor:
                resultado.append(cancion)
        elif campo == "genero":
            if cancion.genero == valor:
                resultado.append(cancion)
    return resultado


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    izquierda = 0
    derecha = len(canciones_ordenadas) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        titulo_medio = canciones_ordenadas[medio].titulo
        if titulo_medio == titulo:
            return canciones_ordenadas[medio]
        elif titulo < titulo_medio:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    raise CancionNoEncontradaError(
        f"No existe una canción con título '{titulo}'"
    )

# Teoría:
# La búsqueda binaria requiere que la lista esté ordenada por título porque en cada paso descarta la mitad de los
# elementos comparando el título buscado con el elemento central.
# Si la lista no estuviera ordenada, no sería posible saber en qué mitad continuar buscando.

# La complejidad de la búsqueda binaria es O(log n).
# La complejidad de la búsqueda lineal por artista es O(n), porque puede ser necesario recorrer todas las canciones.