import json
import os

resources_path = "./resources"
# resources_path = "./"

emojis_dict = []

for r, d, files in os.walk(resources_path):

    for filename in files:
        if filename not in ["emojis.json", "create_emojis_json.py"]:
            with open(f"{resources_path}/{filename}", "r") as f:
                datastore = json.load(f)

                key_1 = list(datastore.keys())[0]

                key_2 = list(datastore[key_1].keys())[0]

                for weird_dict in datastore[key_1][key_2]:
                    emojis_dict.append(weird_dict)

with open(f"{resources_path}/emojis.json", "w") as fp:
    json.dump(emojis_dict, fp)
