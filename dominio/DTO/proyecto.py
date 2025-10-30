class proyecto:
    def __init__(self,nombre,descripcion,fecha_inicio,participantes,director,id_proyecto):
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha_inicio=fecha_inicio
        self.participantes=participantes
        self.director=director
        self.id_proyecto=id_proyecto

    def __str__(self):
        return "Nombre:{}\nDescripcion:{}\nFecha_inicio:{}\nParticipantes:{}\nDirector:{}\nId_proyecto:{}\n"