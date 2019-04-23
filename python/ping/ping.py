import os
import csv
#from colorama import Fore
import time
import datetime

archivo_servidores = 'servidores.csv'

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname + " >/dev/null")
    if response == 0:
        check_ping = "[OK]"
    else:
        check_ping = "[Error]"
 
    return check_ping
 
 
#def sonido_alerta():
#    os.system("play -q ent_communicator1.mp3")
datos_servidores= ''
with open(archivo_servidores, 'rb') as f:
    reader = csv.reader(f)
    datos_servidores = list(reader)

#servidores_reader = csv.reader(archivo_servidores)
#datos_servidores = list(servidores_reader)
contador = 0

while True:
    for i in range(len(datos_servidores)):
        servidorTexto = datos_servidores[i][0]
        servidorIP = datos_servidores[i][1]
        resultado = check_ping(datos_servidores[i][1])
 
        if resultado == "[Error]":
            print("{0:30} {1:17} {2:7}".format(servidorTexto, servidorIP, resultado))
            #sonido_alerta()
        else:
            print("{0:30} {1:17} {2:7}".format(servidorTexto, servidorIP, resultado))
 
    contador += 1
   # print(Fore.BLUE)
    print('{0} {1:%H:%M:%S} {2}'.format(contador, datetime.datetime.now(),"________________________________________"))
    print()
 
    # Pausa de 1 minutos.
    time.sleep(30)

#sonido_alerta()
