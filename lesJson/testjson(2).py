import json
import installation as installer

with open('BDInstall.json') as var: 
	json_data = json.load(var)

	for item in json_data["data"]: 
 		install = installer.Installation(item["InsNumeroInstall"], item["InsNom"], item ["InsNoVoie"], item["InsLibelleVoie"], item["InsCodePostal"], item["ComLib"], item["Latitude"], item["Longitude"]) 

	print(install.display_nom())