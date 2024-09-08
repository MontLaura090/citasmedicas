from calendario import Calendario

class Persona:
    def __init__(self, nombre_completo, cedula, telefono, correo):
        self.nombre_completo = nombre_completo
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo

    def obtener_informacion(self):
        return f"Nombre: {self.nombre_completo}, Cédula: {self.cedula}, Teléfono: {self.telefono}, Correo: {self.correo}"


class Paciente(Persona):
    def __init__(self, nombre_completo, cedula, telefono, correo, historial_medico):
        super().__init__(nombre_completo, cedula, telefono, correo)
        self.historial_medico = historial_medico


class Medico(Persona):
    def __init__(self, nombre_completo, cedula, telefono, correo, especialidad):
        super().__init__(nombre_completo, cedula, telefono, correo)
        self.especialidad = especialidad


