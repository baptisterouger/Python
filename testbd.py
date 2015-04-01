import bd as bd
import json
import modele.equipement as equipement
import modele.activite as activite
import modele.installation as installation


data = bd.bd()
data.creation()
#salle=equipement.Equipement(1532, "salle municipal", 1548)
#print(salle.dysplay_EquipementId())
#data.insertEquipement(salle)
#data.afficheEquipement()

#foot=activite.Activite(25, "foot", 1532)
#data.insertActivite(foot)
#data.afficheActivite()

#nantes=installation.Installation(250, "complexe sportif", 10, "rue de chateaubriand", 44000, "nantes", 1111111, 222222)
#data.insertInstallation(nantes)
#data.afficheInstallation()

with open('lesJson/equipement.json') as data_file:    
    jason = json.load(data_file)
for item in jason['data']:
	equ= equipement.Equipement(item['EquipementId'], item['EquNom'], item['InsNumeroInstall'])
	data.insertEquipement(equ)
print("tous les équipements sont ajoutés !! ")

with open('lesJson/activite.json') as data_file:    
	jason = json.load(data_file)
for item in jason['data']:
	act= activite.Activite(item['ActCode'], item['ActLib'], item['EquipementId'])
	data.insertActivite(act)
print("toutes les activités sont ajoutées !!!")

with open('lesJson/installation.json') as data_file:    
	jason = json.load(data_file)
for item in jason['data']:
	ins= installation.Installation(item['InsNumeroInstall'], item['InsPartLibelle'], item['InsNoVoie'], item['InsLibelleVoie'], item['InsCodePostal'], item['ComLib'], item['Latitude'], item['Longitude'])
	data.insertInstallation(ins)

print("toutes les installations sont ajoutées !!!!")
data.commit()