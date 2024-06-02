from .visuals import *
from .appmanager import manage_apps
import platform

def sys_clear():
    if platform.system() == 'Linux':
        os.system("clear")
    
    else:
        os.system("cls")

def menu(enable_internet):
    while True:
        sys_clear()

        print(p_title)

        menu = input("menu>")

        if menu == 'help':
            print(p_menu_help)
            input()

        elif menu == 'apps':
            print(p_apps_list)
            input()

        elif menu == 'appmanager':
            while True:
                appmanager_menu = input(p_appmanager)
                sys_clear()
                if appmanager_menu == '1':
                    pass

                elif appmanager_menu == '2':
                    if enable_internet["use_internet"] != True:
                        print(e_no_internet)
                    
                    else:
                        manage_apps('https://raw.githubusercontent.com/drwigs/portable_taciyn/main/src/json/git_update.json')

                elif appmanager_menu == '3':
                    break