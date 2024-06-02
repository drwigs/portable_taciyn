import requests
import json
import os

def delete_apps():
    with open('src/json/local_update.json', 'r') as json_local_file:
        json_local_data = json.load(json_local_file)
    
    print("APLICACIONES INSTALADAS:")
    for i in json_local_data["apps"]:
        print("-",i)
        
    app_name = input("Nombre de la aplicación a desinstalar: ")
    if app_name in json_local_data['apps']:
        del json_local_data['apps'][app_name]
        os.remove('apps/'+i+'.py')

    with open('src/json/local_update.json', 'w') as json_mod_local_file:
        json.dump(json_local_data, json_mod_local_file, indent=4)

def manage_apps(update_url):
    with open('src/json/local_update.json', 'r') as json_local_file:
        json_local_data = json.load(json_local_file)
    
    git_update = requests.get(update_url).json()

    print("APLICACIONES INSTALABLES:")
    for i in git_update["apps"]:
        print("-",i)

    app_download = input("Introduce el nombre del programa a instalar> ")
    if app_download in git_update["apps"]:
        url_app_download = requests.get(git_update["apps"][app_download]["url"], stream=True)

        with open(('apps/'+app_download+'.py'),'wb') as file_app_download:
            for chunk in url_app_download.iter_content(chunk_size=8192):
                file_app_download.write(chunk)

        json_local_data['apps'].update({
            app_download: {
                'id': git_update["apps"][app_download]["id"],
                'url': git_update["apps"][app_download]["url"]
            }
        })

        with open('src/json/local_update.json', 'w') as archivo:
            json.dump(json_local_data, archivo, indent=2)

    else:
        print("Programa no encontrado")
