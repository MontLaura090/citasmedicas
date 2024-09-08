class Agenda:
    def __init__(self):
        self.citas = []

    def agregar_cita(self, cita):
        self.citas.append(cita)

    def obtener_citas(self):
        return self.citas
