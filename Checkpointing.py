import pickle
import os

class EstadoEjecucion:
    def __init__(self):
        self.Nombre = None
        self.Fecha = None
def guardar_estado(estado, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(estado, f)
    print("Datos guardados correctamente.")
def cargar_estado(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'rb') as f:
            estado = pickle.load(f)
        print("Datos cargados correctamente.")
        return estado
    else:
        print("No hay datos previos en el archivo.")
        return None

#main
if __name__ == "__main__":
    #verificamos si hay datos guardados en el archivo
    estado_previo = cargar_estado("checkpoint.pkl")
    if estado_previo: #si hay datos, imprimirlos
        print("Datos encontrados:", estado_previo.__dict__)
    else: #si no hay datos, capturarlos
        estado_actual = EstadoEjecucion()
        estado_actual.Nombre = input("Ingrese su nombre: ")
        estado_actual.Fecha = int(input("Ingrese su fecha de cumpleaños (dia): "))
        #guardar datos en un archivo de nombre "checkpoint"
        guardar_estado(estado_actual, "checkpoint.pkl")
        print("Datos guardados:", estado_actual.__dict__)
