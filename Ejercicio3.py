def versiones_de(biblioteca, versiones, cancion_id):
    # Devuelve una lista de tuplas: (titulo, tipo)
    # no incluye la canción original.
    biblioteca.obtener(cancion_id) # Verifica que la canción exista
    directas = []

    for id_version, id_original, tipo in versiones:
        if id_original == cancion_id:
            directas.append((id_version, tipo))

    directas.sort(key=lambda x: x[0]) # La consigna pide recorrerlas de menor a mayor id

    # CASO BASE: No existen versiones directas
    if len(directas) == 0:
        return []
    resultado = []

    # CASO RECURSIVO
    for id_version, tipo in directas:
        cancion = biblioteca.obtener(id_version)
        resultado.append((cancion.titulo, tipo))
        resultado.extend(
            versiones_de(
                biblioteca,
                versiones,
                id_version
            )
        )

    return resultado

# Teoria:
# Caso base:
# Si ninguna cancon tiene como version_de_id al cancion_id recibido,
# la funcion devuelve [].

# versiones_de(..., 12)
# encuentra: 13 (live) y devuelve: [("Ji Ji Ji", "live")] + versiones_de(..., 13)

# versiones_de(..., 13)
# encuentra: 70 (remix) y devuelve: [("Ji Ji Ji (Remix)", "remix")] + versiones_de(..., 70)

# versiones_de(..., 70) no encuentra versiones derivadasy evuelve: []

# Al retornar:
# versiones_de(..., 13) devuelve: [("Ji Ji Ji (Remix)", "remix")]

# versiones_de(..., 12) devuelve: [ ("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix") ]