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
            update_apps_visuals()
            input()

        elif menu == 'apps':
            print(p_apps_list)
            select_app = input("Nombre del programa a abrir: ")
            run_app(select_app)
            input()

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
