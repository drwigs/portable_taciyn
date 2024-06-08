import os
import json
from pysine import sine

with open('src/json/local_update.json') as visual_json_update_data:
    visual_update_data = json.load(visual_json_update_data)

def intro_tune():
    sine(frequency=349, duration=0.3)
    sine(frequency=391, duration=0.3)
    sine(frequency=587, duration=0.5)

p_title = """
------------------------
|        TACIYN        |
|       PORTABLE       |
|     By: dr_wigs      |
------------------------
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

p_press_enter = "Presiona ENTER para continuar..."

p_appmanager_menu = """
1- 
"""

p_apps_list = """
Aplicaciones instaladas:

"""

p_configuration_list = """
[1]: 
"""

def update_apps_visuals():
    if visual_update_data["apps"] == {}:
        print("No hay aplicaciones instaladas")

    else:
        print("Aplicaciones instaladas:")
        for i in visual_update_data["apps"].keys():
            print("-"+i)



