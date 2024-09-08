class Cita:
    def __init__(self, idCita, hora, fecha, paciente, medico):
        self.idCita = idCita
        self.hora = hora
        self.fecha = fecha
        self.paciente = paciente
        self.medico = medico
        self.estado = "Reservada"

    def crear_cita(self):
        return f"Cita creada con ID {self.idCita} para el paciente {self.paciente.nombre_completo} con el médico {self.medico.nombre_completo}."

    def reprogramar_cita(self, nueva_hora, nueva_fecha):
        self.hora = nueva_hora
        self.fecha = nueva_fecha
        return f"Cita {self.idCita} reprogramada para {self.fecha} a las {self.hora}."

