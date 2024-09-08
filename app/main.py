from datetime import datetime
from persona import Paciente, Medico
from cita import Cita
from notificacion import EstrategiaCorreoElectronico, EstrategiaSMS, EstrategiaAppMovil
import os
import pandas as pd
from calendario import Calendario
from reporte import GeneradorReportes, FormatoExcel

class SistemaCitas:
    def __init__(self):
        self.citas = []
        self.calendario = Calendario()

    def gestionar_cita(self, cita):
        self.citas.append(cita)
        return f"Cita {cita.idCita} gestionada."

    def generar_reporte(self):
        generador = GeneradorReportes(self.citas)
        excel = FormatoExcel()
        generador.agregar_formato(excel)
        generador.generarReporte()

    def cancelar_cita(self, idCita):
        cita_a_cancelar = next((cita for cita in self.citas if cita.idCita == idCita), None)
        if cita_a_cancelar:
            self.citas.remove(cita_a_cancelar)
            print(f"Cita con ID {idCita} ha sido cancelada.")
        else:
            print(f"No se encontró ninguna cita con ID {idCita}.")

    def reprogramar_cita(self, idCita, nueva_fecha, nueva_hora):
        cita_a_reprogramar = next((cita for cita in self.citas if cita.idCita == idCita), None)
        if cita_a_reprogramar:
            cita_a_reprogramar.fecha = nueva_fecha
            cita_a_reprogramar.hora = nueva_hora
            print(f"Cita con ID {idCita} ha sido reprogramada a {nueva_fecha} a las {nueva_hora}.")
        else:
            print(f"No se encontró ninguna cita con ID {idCita}.")

    def mostrar_citas(self):
        if not self.citas:
            print("No hay citas registradas.")
        else:
            for cita in self.citas:
                print(f"ID: {cita.idCita}, Paciente: {cita.paciente.nombre_completo}, Médico: {cita.medico.nombre_completo}, Fecha: {cita.fecha}, Hora: {cita.hora}")

class PacienteObservador:
    def actualizar(self):
        return "Paciente observador actualizado."

correo = EstrategiaCorreoElectronico()
sms = EstrategiaSMS()
app_movil = EstrategiaAppMovil()
sistema_citas = SistemaCitas()

medicos_disponibles = [
    Medico("Dra. Ana Lopez", "87654321", "555-5678", "ana@mail.com", "Cardiología"),
    Medico("Dr. Luis Rodriguez", "23456789", "555-9876", "luis@mail.com", "Cardiología"),
    Medico("Dr. Carlos Jiménez", "34567890", "555-1122", "carlos@mail.com", "Cardiología"),
    Medico("Dra. Elena Fernández", "45678901", "555-2233", "elena@mail.com", "Pediatría"),
    Medico("Dr. Mario Gómez", "56789012", "555-3344", "mario@mail.com", "Pediatría"),
    Medico("Dra. Sofia Pérez", "67890123", "555-4455", "sofia@mail.com", "Pediatría"),
    Medico("Dr. Juan Martinez", "78901234", "555-5566", "juan@mail.com", "Dermatología"),
    Medico("Dra. Laura González", "89012345", "555-6677", "laura@mail.com", "Dermatología"),
    Medico("Dr. Ricardo Rivera", "90123456", "555-7788", "ricardo@mail.com", "Dermatología"),
    Medico("Dra. Valentina Morales", "01234567", "555-8899", "valentina@mail.com", "Gastroenterología"),
    Medico("Dr. Hugo Torres", "11223344", "555-9900", "hugo@mail.com", "Gastroenterología"),
    Medico("Dra. Camila Navarro", "22334455", "555-1010", "camila@mail.com", "Gastroenterología"),
    Medico("Dr. Pedro Ruiz", "33445566", "555-2020", "pedro@mail.com", "Endocrinología"),
    Medico("Dra. Beatriz Castillo", "44556677", "555-3030", "beatriz@mail.com", "Endocrinología"),
    Medico("Dr. Antonio Ramírez", "55667788", "555-4040", "antonio@mail.com", "Endocrinología"),
]

def mostrar_menu():
    print("\n--- Sistema de Gestión de Citas Médicas ---")
    print("1. Agendar una cita")
    print("2. Cancelar una cita")
    print("3. Reprogramar una cita")
    print("4. Generar reporte")
    print("5. Mostrar todas las citas")
    print("6. Salir")

def seleccionar_especialidad():
    especialidades = set(medico.especialidad for medico in medicos_disponibles)
    print("\n--- Seleccione una Especialidad ---")
    for i, especialidad in enumerate(especialidades, start=1):
        print(f"{i}. {especialidad}")
    opcion = int(input("Ingrese el número de la especialidad: "))
    especialidad_seleccionada = list(especialidades)[opcion - 1]
    return especialidad_seleccionada

def seleccionar_medico(especialidad):
    medicos = [medico for medico in medicos_disponibles if medico.especialidad == especialidad]
    if len(medicos) > 3:
        medicos = medicos[:3]
    print(f"\n--- Médicos de {especialidad} ---")
    for i, medico in enumerate(medicos, start=1):
        print(f"{i}. {medico.nombre_completo}")
    opcion = int(input("Ingrese el número del médico: "))
    return medicos[opcion - 1]

def mostrar_disponibilidad(medico):
    fechas = sistema_citas.calendario.disponibilidad.keys()
    print(f"\n--- Disponibilidad del médico {medico.nombre_completo} ---")
    for i, fecha in enumerate(fechas, start=1):
        print(f"{i}. {fecha}")
    
    fecha_opcion = int(input("Ingrese el número de la fecha: "))
    fecha_seleccionada = list(fechas)[fecha_opcion - 1]

    horarios = sistema_citas.calendario.disponibilidad[fecha_seleccionada].get(medico, [])
    print(f"\nHorarios disponibles para {medico.nombre_completo} el {fecha_seleccionada}:")
    for i, hora in enumerate(horarios, start=1):
        print(f"{i}. {hora}")

    hora_opcion = int(input("Ingrese el número del horario: "))
    hora_seleccionada = horarios[hora_opcion - 1]
    
    return fecha_seleccionada, hora_seleccionada

def agendar_cita():
    especialidad = seleccionar_especialidad()
    medico = seleccionar_medico(especialidad)
    fecha, hora = mostrar_disponibilidad(medico)
    
    print("\n--- Agendar Cita ---")
    nombre = input("Ingrese su nombre completo: ")
    cedula = input("Ingrese su número de cédula: ")
    telefono = input("Ingrese su teléfono: ")
    correo_electronico = input("Ingrese su correo electrónico: ")
    historial_medico = input("Ingrese su historial médico (resumen): ")

    paciente = Paciente(nombre, cedula, telefono, correo_electronico, historial_medico)

    id_cita = len(sistema_citas.citas) + 1
    cita = Cita(id_cita, hora, fecha, paciente, medico)
    
    if sistema_citas.calendario.marcar_ocupado(fecha, medico, hora):
        sistema_citas.gestionar_cita(cita)
        print(f"Cita {id_cita} agendada exitosamente para {paciente.nombre_completo} con {medico.nombre_completo}.")
        
        guardar_citas_en_excel()

        correo.enviar_notificacion()
        sms.enviar_notificacion()
        app_movil.enviar_notificacion()

def cancelar_cita():
    print("\n--- Cancelar Cita ---")
    id_cita = int(input("Ingrese el ID de la cita a cancelar: "))
    sistema_citas.cancelar_cita(id_cita)

def reprogramar_cita():
    print("\n--- Reprogramar Cita ---")
    id_cita = int(input("Ingrese el ID de la cita a reprogramar: "))
    nueva_fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
    nueva_hora = input("Ingrese la nueva hora (HH:MM): ")
    sistema_citas.reprogramar_cita(id_cita, nueva_fecha, nueva_hora)

def guardar_citas_en_excel():
    archivo_citas = 'citas_agendadas.xlsx'
    if os.path.exists(archivo_citas):
        df = pd.read_excel(archivo_citas)
    else:
        df = pd.DataFrame(columns=["ID Cita", "Fecha", "Hora", "Paciente", "Cédula", "Teléfono", "Médico", "Especialidad", "Estado"])

    nuevas_filas = []
    for cita in sistema_citas.citas:
        nueva_fila = {
            "ID Cita": cita.idCita,
            "Fecha": cita.fecha,
            "Hora": cita.hora,
            "Paciente": cita.paciente.nombre_completo,
            "Cédula": cita.paciente.cedula,
            "Teléfono": cita.paciente.telefono,
            "Médico": cita.medico.nombre_completo,
            "Especialidad": cita.medico.especialidad,
            "Estado": cita.estado
        }
        nuevas_filas.append(nueva_fila)

    df_nuevas_filas = pd.DataFrame(nuevas_filas)
    df = pd.concat([df, df_nuevas_filas], ignore_index=True)
    df.to_excel(archivo_citas, index=False)

def iniciar_sistema():
    fecha_inicio = "07/09/2024"
    fecha_fin = "05/10/2024"
    hora_inicio = "08:00"
    hora_fin = "16:00"
    intervalo_minutos = 20
    sistema_citas.calendario.generar_disponibilidad(fecha_inicio, fecha_fin, medicos_disponibles, hora_inicio, hora_fin, intervalo_minutos)

    # Instancia el generador de reportes con las citas del sistema
    generador = GeneradorReportes(sistema_citas.citas)
    formato_excel = FormatoExcel()
    generador.agregar_formato(formato_excel)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agendar_cita()
        elif opcion == '2':
            cancelar_cita()
        elif opcion == '3':
            reprogramar_cita()
        elif opcion == '4':
            print("Generando reporte...")
            generador.generarReporte()
        elif opcion == '5':
            sistema_citas.mostrar_citas()
        elif opcion == '6':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    iniciar_sistema()
