import pandas as pd
import tabulate as tb
import os

def limpiarPantalla():
    os.system("cls")
    
def pausar():
    print()
    os.system("pause")

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

            print()
            print("-"*100)
            print("Archivo cargado exitosamente.")
            print("-"*100)
            
            pausar()
            
            limpiarPantalla()
            self.info()
            
        except FileNotFoundError:
            print()
            print("-"*100)
            print("Error: Archivo no encontrado.")
            print("-"*100)
        except Exception as e:
            print()
            print("-"*100)
            print(f"Error al cargar el archivo: {e}")
            print("-"*100)

    # Metodo que muestra informacion de los datos
    def info(self):
        if self.datos is None:
            print("Error: No se han cargado datos.")
            return

        print("-"*100)
        print("Información de los datos:")
        print("-"*100)
        
        # Tamaño del DataFrame
        print(f"\nTamaño del DataFrame: (filas, columnas) = {self.datos.shape}\n")

        # Nombres de las columnas
        print("Columnas:")
        for columna in self.datos.columns:
            print(f"  - {columna}")
        print()

        # Cantidad de valores nulos por columna
        print("Valores nulos por columna:")
        for columna in self.datos.columns:
            cantidad_nulos = self.datos[columna].isnull().sum()
            print(f"  - {columna}: {cantidad_nulos} valores nulos")
        print()

        # Tipos de datos por columna
        print("Tipos de datos por columna:")
        for columna, tipo in zip(self.datos.columns, self.datos.dtypes):
            print(f"  - {columna}: {tipo}")
        print()
    
    
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