import json
filename = "factbook-country-profiles.json"
directory_data = "../files/"
with open(directory_data + filename) as json_file:
    donnees = json.load(json_file)
