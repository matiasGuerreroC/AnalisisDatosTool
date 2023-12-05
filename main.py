import os

from src import HerramientaAnalisisDatos as DF

# Variables globales
herramienta = DF.HerramientaAnalisisDatos()

def limpiarPantalla():
    os.system("cls")
    
def pausar():
    print()
    os.system("pause")
    
def mostrarMenu():
    print("------------------------------------------------")
    print("Bienvenido a la Herramienta de Análisis de Datos")
    print("------------------------------------------------")
    print("1. Cargar archivo de datos")
    print("2. Mostrar datos")
    print("3. Mostrar datos estadísticos")
    print("4. Salir")
    print("------------------------------------------------")
    opcion = int(input("Ingrese una opción: "))
    return opcion

def main():
    while True:
        # Se borra la pantalla
        limpiarPantalla()
        
        # Se muestra el menú de opciones
        opcion = mostrarMenu()
        
        # Se borra la pantalla
        limpiarPantalla()
        
        # Se verifica la opción seleccionada
        if opcion == 1:
            archivo = input("Ingrese el nombre del archivo o la ruta relativa/absoluta: ")
            
            # Convertir a ruta absoluta si es relativa
            archivo = os.path.abspath(archivo)

            formato = input("Ingrese el formato del archivo: ")
            separador = input("Ingrese el separador del archivo: ")
            
            herramienta.cargar_archivo(archivo, formato, separador)
        elif opcion == 2:
            print("-"*100)
            print("Mostrar datos")
            print("-"*100)
            
            print()
            cantidad = int(input("Ingrese la cantidad de datos que desea mostrar: "))
            
            herramienta.mostrar_datos(cantidad)
        elif opcion == 3:
            print("Mostrar datos estadísticos")
            
            herramienta.mostrar_datos_estadisticos()
        elif opcion == 4:
            print("Salir")
            break
        else:
            print("Opción inválida")
        
        # Se pausa la pantalla
        pausar()
        
        # Se borra la pantalla
        limpiarPantalla()
    

if __name__ == "__main__":
    main()