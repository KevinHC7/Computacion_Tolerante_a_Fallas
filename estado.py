#Hernández Cortez Kevin Uriel - 217734547
#Computación Tolerante a Fallas - 25/02/24
import win32serviceutil
import win32service
#-----------------------------------------------------------------------------
def obtenerEstadoServicio(nombreServicio):
  try:
    estadoServicio = win32serviceutil.QueryServiceStatus(nombreServicio)
    if estadoServicio[1] == win32service.SERVICE_RUNNING:
      return "En ejecución"
    elif estadoServicio[1] == win32service.SERVICE_STOPPED:
      return "Detenido"
    else:
      return "Desconocido"
  except win32service.error as e:
    return f"Error: {e.strerror}"
#-----------------------------------------------------------------------------
def main():
  nombreServicio = input("Introduzca el nombre del servicio: ")
  estadoServicio = obtenerEstadoServicio(nombreServicio)
  print(f"El servicio '{nombreServicio}' está {estadoServicio}")

if __name__ == "__main__":
  main()
#-----------------------------------------------------------------------------