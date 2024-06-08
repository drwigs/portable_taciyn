import platform
import os
import json
import sys

# Estilo
from rich.console import Console # type: ignore
from rich.text import Text # type: ignore

# Archivos locales
from .visuals import *
from .appmanager import manage_apps, delete_apps, update_apps
from .startapp import run_app

console = Console()


def sys_clear():
    if platform.system() == 'Linux':
        os.system("clear")
    
    else:
        os.system("cls")

def menu(enable_internet):
    while True:
        sys_clear()
        console.print(p_title, justify="center")


        menu = input("menu>")

        if menu == 'help':
            print(p_menu_help)
            input(p_press_enter)

        elif menu == 'apps':
            update_apps()
            print("----------\n"+"Escribe x Para rechazar")
            select_app = input("Nombre del programa a abrir: ")
            if select_app != 'x':
                while True:
                    inst_open_app = input("Abrir programa? (y/n): ")
                    if inst_open_app == 'y':
                        run_app(select_app)
                        break

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
                    if enable_internet["use_internet"] != "true":
                        print(e_no_internet)
                    
                    else:
                        manage_apps('https://raw.githubusercontent.com/drwigs/portable_taciyn/main/src/json/git_update.json')

                elif appmanager_menu == '3':
                    break

        elif menu == 'exit':
            exit()




