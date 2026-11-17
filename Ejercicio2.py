class CancionNoEncontradaError(Exception):
    def __init__(self, id_cancion):
        super().__init__(f"No existe una canción con id {id_cancion}")


class Biblioteca:
    def __init__(self):
        self.canciones = []
    def agregar(self, cancion):
        self.canciones.append(cancion)
    def cantidad(self):
        return len(self.canciones)
    def obtener(self, id): # Busca una canción por id. Si la encuentra, devuelve el objeto Cancion. Si no la encuentra, lanza la excepción CancionNoEncontradaError.
        for cancion in self.canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(id)
    def listar(self):
        return [str(cancion) for cancion in self.canciones]
    def __iter__(self):
        return iter(self.canciones)

# Teoría:
# La biblioteca almacena todas las canciones disponibles del sistema.
# actua como catálogo general.
# Una playlist almacena solamente una selección.