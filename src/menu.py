import platform
import os
import sys
from .visuals import *
from .appmanager import manage_apps, delete_apps
from .startapp import run_app


def sys_clear():
    if platform.system() == 'Linux':
        os.system("clear")
    
    else:
        os.system("cls")

    print(p_title)

def menu(enable_internet):
    while True:
        sys_clear()

        menu = input("menu>")

        if menu == 'help':
            print(p_menu_help)
            input(p_press_enter)

        elif menu == 'apps':
            update_apps_visuals()
            print("----------\n"+"Escribe x Para rechazar")
            select_app = input("Nombre del programa a abrir: ")
            if select_app != 'x':
                while True:
                    inst_open_app = input("Abrir programa ahora? (y/n): ")
                    if inst_open_app == 'y':
                        run_app(select_app)

                    elif inst_open_app == 'n':
                        break

                    else:
                        print("Respuesta no válida")

            input(p_press_enter)

        elif menu == 'appmanager':
            while True:
                appmanager_menu = input(p_appmanager)
                sys_clear()
                if appmanager_menu == '1':
                    delete_apps()

                elif appmanager_menu == '2':
                    if enable_internet["use_internet"] != True:
                        print(e_no_internet)
                    
                    else:
                        manage_apps('https://raw.githubusercontent.com/drwigs/portable_taciyn/main/src/json/git_update.json')

                elif appmanager_menu == '3':
                    break

        elif menu == 'configuration':
            pass

        elif menu == 'exit':
            exit()



