class PilaVaciaError(Exception):
    def __init__(self):
        super().__init__("La pila está vacía")


class Pila:
    def __init__(self):
        self.datos = ListaEnlazada()

    def apilar(self, dato): # tope siempre el primer nodo
        self.datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError()
        return self.datos.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError()
        return self.datos.primero.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self.historial = Pila()

    def registrar(self, cancion):
        self.historial.apilar(cancion)

    def anterior(self):
        return self.historial.desapilar()

    def ultima(self):
        return self.historial.ver_tope()

# Teoría:
# El primer anterior() devuelve "De Música Ligera".
# Esto ocurre porque en una pila, el último elemento apilado es el primero que se desapila.
# Por lo tanto, el tope de la pila es "De Música Ligera" y es el primer elemento devuelto por anterior().