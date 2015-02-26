import json 
import 

with open("BDInstall.json") as var: 
	json_data = json.loads(var.read())

	for item in json_data["InsNumeroInstall"]: 
 		install = Installation(item["InsNumeroInstall"], item["InsNom"], item ["InsNoVoie" + "InsLibelleVoie"]) +