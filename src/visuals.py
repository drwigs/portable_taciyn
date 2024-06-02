import os
import json

with open('src/json/local_update.json') as visual_json_update_data:
    visual_update_data = json.load(visual_json_update_data)

p_title = """
TACIYN """+str(visual_update_data["update_id"])+"""
PORTABLE =)
"""

e_no_internet = """
Sin conexión a internet.

-No se podrán actualizar
los archivos.
-Las funciones de red
están deshabilitadas.
-No se podrán instalar
aplicaciones.
"""

p_menu_help = """
Estás en el menú de Taciyn.

-help: Ver información acerca
de los comandos introducibles
en el menú.

-apps: Muestra una lista de
aplicaciones instaladas.

-appmanager: Abre el administrador
de aplicaciones.

-exit: Salir del programa.
"""

p_appmanager = """
Administrador de aplicaciones:
1- Eliminar aplicación
2- Instalar aplicación de la red
3- Salir
>"""

p_appmanager_menu = """
1- 
"""

p_apps_list = """
Aplicaciones instaladas:

"""

def update_apps_visuals():
    if visual_update_data["apps"] == {}:
        print("No hay aplicaciones instaladas")

    else:
        print("Aplicaciones instaladas:")
        for i in visual_update_data["apps"].keys():
            print("-"+i)
