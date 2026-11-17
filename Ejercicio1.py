class Cancion:
    def __init__(señf, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id=id
        self.titulo=titulo
        self.artista=artista
        self.album=album
        self.genero=genero
        self.anio=anio
        self.duracion_seg=duracion_seg

    def duracion_mmss(self):
        minutos=self.duracion_seg//60
        segundos=self.duracion_seg%60
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return (
            f"#{self.id} {self.titulo} | "
            f"{self.artista} | "
            f"{self.anio} | "
            f"{self.duracion_mmss()}"
        )

    def __eq__(self, other):
        if not isinstance(other, Cancion):
            return False
        return self.id == other.id

# conviene guardar la duracion como un entero porque de este modo 
# permite realizar calculos o comparaciones u ordenamientos de 
# manera mas simple. Si se guarda como str, habria que 
# convertirlo antes para poder operar con la duracion.