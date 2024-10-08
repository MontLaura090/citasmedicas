Sistema de Gestión de Citas Médicas
Este proyecto es un sistema de gestión de citas médicas que permite agendar, cancelar y reprogramar citas, además de generar reportes en formato Excel.

Requisitos
Para ejecutar este programa, necesitas tener instalado Python 3.x y las siguientes bibliotecas:

pandas para la manipulación de datos y trabajo con archivos Excel.
openpyxl para leer y escribir archivos Excel en formato .xlsx.

Instalación
Clona este repositorio o descarga el código fuente:
git clone <URL_DEL_REPOSITORIO>
cd nombre_del_repositorio

Crea y activa un entorno virtual (opcional pero recomendado):

Para crear un entorno virtual:
python -m venv mi_entorno
mi_entorno\Scripts\activate


Archivos y Módulos
Asegúrate de que los siguientes archivos estén presentes en tu directorio de trabajo:

persona.py: Contiene las clases Paciente y Medico.
cita.py: Contiene la clase Cita.
notificacion.py: Contiene las clases EstrategiaCorreoElectronico, EstrategiaSMS, y EstrategiaAppMovil.
calendario.py: Contiene la clase Calendario.
reporte.py: Contiene las clases GeneradorReportes y FormatoExcel.

Ejecución
Guarda el código principal en un archivo llamado main.py.

python main.py

Archivos de Datos
El programa generará un archivo Excel llamado citas_agendadas.xlsx en el directorio de trabajo. Este archivo contiene los datos de las citas agendadas y se actualizará automáticamente con cada nueva cita.