import requests
import json
from time import sleep
import os

update_modules = []

git_update = None

def setup_update(setup_update_type, setup_update_url, git_json, file_name):
    os.remove(setup_update_type+'/'+file_name+'.py')
    with open((setup_update_type+'/'+file_name+'.py'),'wb') as file_app_download:
        for chunk in requests.get(setup_update_url).iter_content(chunk_size=8192):
            file_app_download.write(chunk)
        
        with open('src/json/local_update.json', 'r') as json_local_file:
            json_local_data = json.load(json_local_file)
        json_local_data[setup_update_type][file_name]["id"] = git_json[setup_update_type][file_name]["id"]

        with open('src/json/local_update.json', 'w') as json_id_file:
            json.dump(json_local_data, json_id_file)



def manage_updates(update_type, update_url, auto_update):
    with open('src/json/local_update.json', 'r') as json_local_file:
        json_local_data = json.load(json_local_file)

    git_update = requests.get(update_url).json()

    for i in git_update[update_type]:
        if git_update[update_type][i]["id"] != json_local_data[update_type][i]["id"]:
            update_modules.append(i)


    if len(update_modules) > 0:
        print("¡Se ha encontrado una actualización en uno de los módulos!")
        
        if auto_update == True:
            for j in update_modules:
                setup_update(update_type, git_update[update_type][j]["url"], git_update, j)
        
        else:
            while True:
                continue_update = input("Descargar? y/n>")
                while True:
                    if continue_update == 'y':
                        for j in update_modules:
                            setup_update(update_type, git_update[update_type][j]["url"], git_update, j)
                            print("Módulo '"+j+"' actualizado con éxito")
                        break

                    elif continue_update == 'n':
                        break

                    else:
                        break
                
                break
        
    else:
        print("Sin actualizaciones.")
        sleep(1)

