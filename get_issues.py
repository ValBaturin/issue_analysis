import requests
import json
import os

from config import ISSUE_PATH

url = 'https://bugzilla.mozilla.org/rest/product/firefox'
response = requests.get(url)
data = response.json()
components = data["products"][0]["components"]
for i in range(len(components)):
    dir_path = ISSUE_PATH + str(i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    component_description = components[i]["description"]
    if not os.path.exists(dir_path + "/label"):
        with open(dir_path + "/label", 'w') as out:
            print(component_description, file=out)
    issues_flags = components[i]["flag_types"]
    for bug in issues_flags["attachment"]:
        name = bug["id"]
        path = dir_path + "/" + str(name)
        if not os.path.exists(path):
            with open(path, 'w') as out:
                description = bug["description"]
                print(description, file=out)
