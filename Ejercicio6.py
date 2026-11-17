class ColaVaciaError(Exception):
    def __init__(self):
        super().__init__("La cola está vacía")


class Cola:
    def __init__(self):
        self.datos = ListaEnlazada()

    def encolar(self, dato):
        self.datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError()
        return self.datos.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError()
        return self.datos.primero.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class ColaReproduccion:
    def __init__(self):
        self.cola = Cola()

    def encolar_cancion(self, cancion):
        self.cola.encolar(cancion)

    def siguiente(self):
        return self.cola.desencolar()

    def que_sigue(self):
        return self.cola.ver_frente()

# Teoría:
# El primer siguiente() devuelve "Jijiji".
# Esto sucede porque en la cola, el primer elemento que entra es el primero que sale.
# Por lo tanto, el primer siguiente() devuelve Jijiji.
