import os
import requests
import json
import socket

AUTH_UPDATE = 'https://pastebin.com/raw/U6xyBbf1' # Autorización de actualización y versión

UPDATE_CONFIGURATION = 'https://raw.githubusercontent.com/drwigs/portable_taciyn/main/src/json/local_update.json'

GIT_UPDATE_CONFIGURATION = 'https://raw.githubusercontent.com/drwigs/portable_taciyn/main/src/json/git_update.json'

UPDATE_ID = 1

main_configuration = {
    'use_internet': True,
    'auto_updates': False
}


"""
Se creará el entorno donde se
desarrollará el programa y se
instalaran los archivos necesarios
o complementarios para que funcione
"""

if not 'apps' in os.listdir():
    os.makedirs('apps')

if not 'src' in os.listdir():
    os.makedirs('src')
    os.makedirs('src/json')

"""
Comprueba que el dispositivo
puede conectarse a internet, en
caso contrario, el programa se
ejecutará sin internet.
"""

net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
net.settimeout(5)
try:
	net.connect(("google.com", 80))

except (socket.gaierror, socket.timeout):
	print(e_no_internet)
	main_configuration['use_internet'] = False

"""
Se verificará si existe el archivo
auth_update.json, en caso contrario
se creará y posteriormente se descargará
su contenido de la url de actualizaciones.
"""

if not 'local_update.json' in os.listdir('src/json'):
    # Conecta con la URL de las actualizaciones
    update_response = requests.get(UPDATE_CONFIGURATION)

    with open('src/json/local_update.json', mode="wb") as write_update_data:
        write_update_data.write(update_response.content)
    
    del update_response
    del write_update_data

with open('src/json/local_update.json') as json_update_data:
    update_data = json.load(json_update_data)


"""
Comprueba que no hay actualizaciones nuevas
viendo la ID del archivo actual y la ID
de los archivos del git
"""

update_response = requests.get(UPDATE_CONFIGURATION)

"""
Crea el archivo JSON local
en donde viene toda la
información de los módulos,
en caso de que no exista.
"""

if not 'local_update.json' in os.listdir('src/json/'):
    with open('src/json/local_update.json', mode="wb") as write_update_data:
        write_update_data.write(update_response.content)

"""
Encontrar el módulo requests, cuya
función es descargar archivos adicionales
y actualizaciones posteriores.

En caso de que no, descargará el módulo
con pip.

(Válido para Windows y Pydroid3/Linux)
"""

try:
    import requests

except ModuleNotFoundError:
    os.system("pip install requests")

"""
Aquí se encarga de verificar si
los archivos requeridos para el programa
se encuentran, en caso de que no
los descargará desde github/wigsGrammani
"""

try:
    from src.visuals import *

except ModuleNotFoundError:
    if main_configuration['use_internet'] != True:
        exit()

    file_src = requests.get(update_data['src']['visual']['url'])

    with open(('src/visuals.py'),'wb') as file_src_download:
        for chunk in file_src.iter_content(chunk_size=8192):
            file_src_download.write(chunk)
    from src.visuals import *


try:
    from src.appmanager import *

except ModuleNotFoundError:
    if main_configuration['use_internet'] != True:
        exit()
    file_src = requests.get(update_data['src']['appmanager']['url'])

    with open(('src/appmanager.py'),'wb') as file_src_download:
        for chunk in file_src.iter_content(chunk_size=8192):
            file_src_download.write(chunk)

    from src.appmanager import *


try:
    from src.updates import *

except ModuleNotFoundError:
    if main_configuration['use_internet'] != True:
        exit()

    file_src = requests.get(update_data['src']['updates']['url'])

    with open(('src/updates.py'),'wb') as file_src_download:
        for chunk in file_src.iter_content(chunk_size=8192):
            file_src_download.write(chunk)
    
    from src.updates import *


try:
    from src.menu import *

except ModuleNotFoundError:
    if main_configuration['use_internet'] != True:
        exit()

    file_src = requests.get(update_data['src']['menu']['url'])

    with open(('src/menu.py'),'wb') as file_src_download:
        for chunk in file_src.iter_content(chunk_size=8192):
            file_src_download.write(chunk)


try:
    from src.startapp import *

except ModuleNotFoundError:
    if main_configuration['use_internet'] != True:
        exit()

    file_src = requests.get(update_data['src']['startapp']['url'])

    with open(('src/startapp.py'),'wb') as file_src_download:
        for chunk in file_src.iter_content(chunk_size=8192):
            file_src_download.write(chunk)

"""
Se verificará si hay actualizaciones
en los archivos src
"""

manage_updates('src', GIT_UPDATE_CONFIGURATION, main_configuration['auto_updates'])


print(p_title)


"""
Iniciará el menú con las configuraciones
establecidas
"""

menu(main_configuration)