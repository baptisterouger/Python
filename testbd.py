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
for item in jason:
	equipement=equipement.Equipement(int(item['EquipementId']), item['EquNom'], int(item['InsNumeroInstall']))
	data.insertEquipement(equipement)
	print("ligne ajoutée"+equipement.dysplay_EquipementId())