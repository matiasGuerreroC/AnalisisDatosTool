import pandas as pd
import tabulate as tb

class HerramientaAnalisisDatos:
    def __init__(self):
        self.datos = None  # Atributo para almacenar los datos

    def cargar_archivo(self, archivo, formato=None, separador=None):
        try:
            if formato is None:
                self.datos = pd.read_file(archivo, sep=separador)
            elif formato.lower() == 'csv':
                self.datos = pd.read_csv(archivo, sep=separador)
            elif formato.lower() in ['excel', 'xls', 'xlsx']:
                self.datos = pd.read_excel(archivo, sep=separador)
            elif formato.lower() == 'json':
                self.datos = pd.read_json(archivo, sep=separador)
            else:
                print(f"Error: Formato no admitido: {formato}")
                return

            print("Archivo cargado exitosamente.")
        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

    def mostrar_datos(self, cantidad):
        if self.datos is None:
            print("Error: No se han cargado datos.")
            return

        print(tb.tabulate(self.datos.head(cantidad), headers='keys', tablefmt='pretty'))
        
    def mostrar_datos_estadisticos(self):
        if self.datos is None:
            print("Error: No se han cargado datos.")
            return
        
        print(tb.tabulate(self.datos.describe(), headers='keys', tablefmt='pretty'))