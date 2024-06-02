import os

from .updates import manage_updates

GIT_UPDATE_CONFIGURATION = 'https://raw.githubusercontent.com/drwigs/portable_taciyn/main/src/json/git_update.json'

def run_app(app_name):
    if app_name+".py" in os.listdir('apps/'):
        manage_updates('apps', GIT_UPDATE_CONFIGURATION, False)
        os.system("python3 apps/multiop.py")
        print("Programa "+app_name+" finalizado")
    
    else:
        print(os.listdir('apps/'))
        print("Programa no encontrado.")