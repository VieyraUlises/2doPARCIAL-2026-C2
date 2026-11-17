from Ejercicio1 import Cancion
from Ejercicio2 import Biblioteca


class ArchivoInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


def guardar_canciones_csv(ruta, biblioteca):
    encabezado = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]

    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)

        for cancion in biblioteca:
            escritor.writerow([
                cancion.id,
                cancion.titulo,
                cancion.artista,
                cancion.album,
                cancion.genero,
                cancion.anio,
                cancion.duracion_seg
            ])


def cargar_canciones_csv(ruta):
    encabezado = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]
    biblioteca = Biblioteca()

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)

            encabezado_archivo = next(lector, None)

            if encabezado_archivo != encabezado:
                raise ArchivoInvalidoError("El encabezado del archivo es incorrecto")

            for fila in lector:
                if len(fila) < 7:
                    raise ArchivoInvalidoError("Una fila tiene menos de 7 columnas")

                cancion = Cancion(
                    int(fila[0]),
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    int(fila[5]),
                    int(fila[6])
                )

                biblioteca.agregar(cancion)

    except FileNotFoundError:
        raise ArchivoInvalidoError("El archivo no existe")

    return biblioteca