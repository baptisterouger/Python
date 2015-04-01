import cherrypy
import json
import bd as bd

from mako.template import Template
from mako.lookup import TemplateLookup
 
lookup = TemplateLookup(directories=[""]) 

#data = json.loads(open("BDInstall.json").read())


class WebManager(object):
    
	@cherrypy.expose
	def index(self):
		return "<h1>Bienvenue sur mon serveur CherryPy</h1>"

	@cherrypy.expose
	def equipement(self):
		b = bd.bd()
		liste = b.afficheEquipement()
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows=[[equipement.display_EquipementId(), equipement.display_EquNom()] for equipement in liste]		) 

	@cherrypy.expose	
	def activite(self):
		b = bd.bd()
		liste = b.afficheActivite()
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows=[[activite.display_ActLib()] for activite in liste]		) 


	@cherrypy.expose
	def installation(self):
		b = bd.bd()
		liste = b.afficheInstallation()
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows=[[installation.get_InsPartLibelle()] for installation in liste]
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
		view = Template(filename="template.html", lookup=lookup)
		return view.render(
			rows=[[installation[0]] for installation in liste]
		) 

	@cherrypy.expose
	def installationParVille(self, ville):
		b = bd.bd()
		liste = b.afficheInstallationParVille(ville)
		view = Template(filename="template2.html", lookup=lookup)
		return view.render(
			rows=[[installation[0]] for installation in liste]
		) 



cherrypy.quickstart(WebManager())