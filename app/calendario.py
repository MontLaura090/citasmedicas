import random
from datetime import datetime, timedelta

class Calendario:
    def __init__(self):
        self.disponibilidad = {}

    def generar_disponibilidad(self, fecha_inicio, fecha_fin, medicos, hora_inicio, hora_fin, intervalo_minutos):
        fecha_actual = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_final = datetime.strptime(fecha_fin, "%d/%m/%Y")
        while fecha_actual <= fecha_final:
            fecha_str = fecha_actual.strftime("%d/%m/%Y")
            self.disponibilidad[fecha_str] = {}
            hora_actual = datetime.strptime(hora_inicio, "%H:%M")
            hora_final = datetime.strptime(hora_fin, "%H:%M")
            while hora_actual < hora_final:
                for medico in medicos:
                    if medico not in self.disponibilidad[fecha_str]:
                        self.disponibilidad[fecha_str][medico] = []
                    self.disponibilidad[fecha_str][medico].append(hora_actual.strftime("%H:%M"))
                hora_actual += timedelta(minutes=intervalo_minutos)
            fecha_actual += timedelta(days=1)
        print(f"Disponibilidad generada del {fecha_inicio} al {fecha_fin}")

    def mostrar_calendario(self, fecha):
        if fecha not in self.disponibilidad:
            print("No hay disponibilidad registrada para esta fecha.")
        else:
            print(f"Disponibilidad para {fecha}:")
            for medico, horarios in self.disponibilidad[fecha].items():
                print(f"{medico.nombre_completo} ({medico.especialidad}): {', '.join(horarios)}")

    def marcar_ocupado(self, fecha, medico, hora):
        if fecha in self.disponibilidad and medico in self.disponibilidad[fecha]:
            if hora in self.disponibilidad[fecha][medico]:
                self.disponibilidad[fecha][medico].remove(hora)
                print(f"Hora {hora} marcada como ocupada para {medico.nombre_completo} en {fecha}")
                return True
        return False
