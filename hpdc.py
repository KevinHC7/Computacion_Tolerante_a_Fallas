#Hernández Cortez Kevin Uriel
#Programa que usa hilos, procesos, demonios y concurrencia.
import threading
import multiprocessing
import concurrent.futures
import time
#-----------------------------------------------------
#funcion para ejecutar en un hilo
def funcionHilo(name):
    print(f"Hilo {name} iniciado")
    time.sleep(2)
    print(f"Hilo {name} terminado")
#funcion para ejecutar en un proceso
def funcionProceso(name):
    print(f"Proceso {name} iniciado")
    time.sleep(2)
    print(f"Proceso {name} terminado")
#funcion para ejecutar en una tarea concurrente
def funcionConcurrente(name):
    print(f"Tarea concurrente {name} iniciada")
    time.sleep(2)
    print(f"Tarea concurrente {name} terminada")
#funcion para ejecutar como demonio
def funcionDemonio():
    while True:
        #tareas que podría hacer el demonio
        print("Demonio ejecutandose...")
        time.sleep(1)
#-----------------------------------------------------
if __name__ == "__main__":
    #creamos y ejecutamos un proceso "demonio"
    daemon_process = multiprocessing.Process(target=funcionDemonio)
    daemon_process.daemon = True  #aqui se indica que es un demonio
    daemon_process.start()
    #ejecutamos hilos
    for i in range(3):
        thread = threading.Thread(target=funcionHilo, args=(i,))
        thread.start()
    #ejecutamos procesos
    for i in range(3):
        process = multiprocessing.Process(target=funcionProceso, args=(i,))
        process.start()
    #ejecutamos tareas concurrentes
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(funcionConcurrente, i) for i in range(3)]
        concurrent.futures.wait(futures)

    print("Exito!")
#-----------------------------------------------------