class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self.primero = Nodo(dato, self.primero)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def quitar_primero(self):
        if self.esta_vacia():
            return None
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._tamanio -= 1
        return dato

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self.canciones = ListaEnlazada()

    def agregar(self, cancion):
        self.canciones.insertar_al_final(cancion)

    def quitar(self, id):
        anterior = None
        actual = self.canciones.primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self.canciones.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.canciones._tamanio -= 1
                return actual.dato
            anterior = actual
            actual = actual.siguiente
        raise CancionNoEncontradaError(id)

    def listar(self):
        return [str(cancion) for cancion in self.canciones]

    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion_seg
        return total

# Teoría:
# Si la lista solo guarda una referencia al primer nodo, para insertar al final cuando hay n elementos se deben
# recorrer los n nodos hasta llegar al último. O sea que el costo es O(n).