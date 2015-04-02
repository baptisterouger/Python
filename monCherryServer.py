import cherrypy
import json
import bd as bd
import modele.equipement as equipement
import modele.activite as activite
import modele.installation as installation

from mako.template import Template
from mako.lookup import TemplateLookup
 
lookup = TemplateLookup(directories=[""]) 

#data = json.loads(open("BDInstall.json").read())


data = bd.bd()
data.creation()

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



class WebManager(object):

	@cherrypy.expose
	def index(self):
		return Template(filename="index.html", lookup=lookup).render()

	@cherrypy.expose
	def equipement(self):
		b = bd.bd()
		liste = b.afficheEquipement()
		view = Template(filename="template2.html", lookup=lookup)
		return view.render(
			titre=[["Id equipement", "nom equipement", "Id installation"]], 
			liste=[[equipement.display_EquipementId(), equipement.display_EquNom(), equipement.display_InsNumeroInstall()] for equipement in liste]		) 

	@cherrypy.expose	
	def activite(self):
		b = bd.bd()
		liste = b.afficheActivite()
		view = Template(filename="template2.html", lookup=lookup)
		return view.render(
			titre=[["Id activite", "Nom activite", "equipId"]], 
			liste=[[activite.display_ActCode(), activite.display_ActLib(), activite.display_EquipementId()] for activite in liste], 
					) 


	@cherrypy.expose
	def installation(self):
		b = bd.bd()
		liste = b.afficheInstallation()
		view = Template(filename="template2.html", lookup=lookup)
		return view.render(
			titre=[["Nom", "Id", "adresse", "Code Postal", "ville", "Lattitude", "Longitude"]], 
			liste=[[installation.get_InsPartLibelle(), installation.get_InsNumeroInstall(), installation.get_adresse(), installation.get_InsCodePostal(), installation.get_ComLib(), installation.get_Latitude(), installation.get_Longitude()] for installation in liste]
		) 
	
	@cherrypy.expose
	def equipementLib(self):
		b = bd.bd()
		liste = b.afficheEquipementLib()
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows=[[equipement[0]] for equipement in liste]
		)

	@cherrypy.expose
	def activiteLib(self):
		b = bd.bd()
		liste = b.afficheActiviteLib()
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows=[[activite[0]] for activite in liste]
		) 

	@cherrypy.expose
	def installationVille(self):
		b = bd.bd()
		liste = b.afficheInstallationVille()
		view = Template(filename="ville.html", lookup=lookup)
		return view.render(
			rows=[[installation[0]] for installation in liste]
		) 

	@cherrypy.expose
	def installationParVille(self, ville):
		b = bd.bd()
		liste = b.afficheInstallationParVille(ville)
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows=[[installation[0]] for installation in liste]
		) 

	@cherrypy.expose
	def recherche(self):
		b = bd.bd()
		liste = b.afficheInstallationVille()
		liste2 = b.afficheEquipementLib()
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows= liste, 
			equip =liste2
		) 

		
	@cherrypy.expose
	def equipParVilleAct(self, ville, activite):
		b = bd.bd()
		if ville == "all":
			titre1=[["rien", "rien"]]
			result = b.afficheEquipement()
			liste1=[[equipement.display_EquipementId(), equipement.display_EquNom()] for equipement in result] 
			
		elif activite == "all":
			titre1=[["rien", "rien", "rien"]]
			liste1 = b.actParVille(ville)

		else:
			titre1=[["rien", "rien", "rien"]]
			liste1 = b.afficheInstallationParVilleParAct(ville, activite)

		view = Template(filename="template2.html", lookup=lookup)
		return view.render(
			titre = titre1,
			liste = liste1
		)


cherrypy.quickstart(WebManager())