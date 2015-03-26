import sqlite3
import modele.equipement as equipement
import modele.activite as activite
import modele.installation as installation

class bd:
	def __init__(self):
		self.conn = sqlite3.connect('data.db')
		self.c = self.conn.cursor()
	def creation(self):
		self.c.execute("DROP TABLE IF EXISTS installation")
		self.c.execute('''CREATE TABLE installation
		             (InsNumeroInstall integer, InsPartLibelle text, InsNoVoie integer, InsLibelleVoie text, InsCodePostal integer, ComLib text, Latitude integer, Longitude integer)''')

		self.c.execute("DROP TABLE IF EXISTS equipement")
		self.c.execute('''CREATE TABLE equipement
		             (EquipementId integer, EquNom text, InsNumeroInstall integer)''')

		self.c.execute("DROP TABLE IF EXISTS activite")
		self.c.execute('''CREATE TABLE activite
		             (ActCode integer, ActLib text, EquipementId integer)''')

		self.conn.commit()

	def insertEquipement(self, equipement):
		self.c.execute("INSERT INTO equipement VALUES (?, ?, ?)", (equipement.dysplay_EquipementId(), equipement.dysplay_EquNom(), equipement.dysplay_InsNumeroInstall()))
		self.conn.commit()
		

	def afficheEquipement(self):
		for row in self.c.execute('SELECT * FROM equipement ORDER BY EquNom'):
			print(row)		

	def insertActivite(self, activite):
		self.c.execute("INSERT INTO activite VALUES(?, ?, ?)", (activite.dysplay_ActCode(), activite.dysplay_ActLib(), activite.dysplay_EquipementId()))
		self.conn.commit()
		
	def afficheActivite(self):
		for row in self.c.execute('SELECT * FROM activite ORDER BY ActLib'):
			print(row)

	def insertInstallation(self, installation):
		self.c.execute("INSERT INTO installation VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (installation.get_InsNumeroInstall(), installation.get_InsPartLibelle(), installation.get_InsNoVoie(), installation.get_InsLibelleVoie(), installation.get_InsCodePostal(), installation.get_ComLib(), installation.get_Latitude(), installation.get_Longitude()))
		self.conn.commit()
		
	def afficheInstallation(self):
		for row in self.c.execute('SELECT * FROM installation ORDER BY InsNumeroInstall'):
			print(row)