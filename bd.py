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
		             (InsNumeroInstall text, InsPartLibelle text, InsNoVoie text, InsLibelleVoie text, InsCodePostal text, ComLib text, Latitude real, Longitude real)''')

		self.c.execute("DROP TABLE IF EXISTS equipement")
		self.c.execute('''CREATE TABLE equipement
		             (EquipementId text, EquNom text, InsNumeroInstall text)''')

		self.c.execute("DROP TABLE IF EXISTS activite")
		self.c.execute('''CREATE TABLE activite
		             (ActCode text, ActLib text, EquipementId text)''')

		self.conn.commit()

	def insertEquipement(self, equipement):
		self.c.execute("INSERT INTO equipement VALUES (?, ?, ?)", (equipement.display_EquipementId(), equipement.display_EquNom(), equipement.display_InsNumeroInstall()))
		
		

	def afficheEquipement(self):
		results = self.c.execute('SELECT * FROM equipement ORDER BY EquNom')
		tab=[]
		for row in results:
			equ= equipement.Equipement(row[0], row[1], row[2])
			tab.append(equ)
		return tab

	def afficheEquipementLib(self):
		results = self.c.execute('SELECT DISTINCT EquNom FROM equipement')
		return results

	def insertActivite(self, activite):
		self.c.execute("INSERT INTO activite VALUES(?, ?, ?)", (activite.display_ActCode(), activite.display_ActLib(), activite.display_EquipementId()))
		
		
	def afficheActivite(self):
		results = self.c.execute('SELECT * FROM activite ORDER BY ActLib')
		tab=[]
		for row in results:
			act= activite.Activite(row[0], row[1], row[2])
			tab.append(act)
		return tab

	def afficheActiviteLib(self):
		results = self.c.execute('SELECT DISTINCT ActLib FROM activite')
		return results

	def insertInstallation(self, installation):
		self.c.execute("INSERT INTO installation VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (installation.get_InsNumeroInstall(), installation.get_InsPartLibelle(), installation.get_InsNoVoie(), installation.get_InsLibelleVoie(), installation.get_InsCodePostal(), installation.get_ComLib(), installation.get_Latitude(), installation.get_Longitude()))
		
		
	def afficheInstallation(self):
		results = self.c.execute('SELECT * FROM installation ORDER BY InsNumeroInstall')
		tab=[]
		for row in results:
			ins= installation.Installation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
			tab.append(ins)
		return tab

	def afficheInstallationVille(self):
		results = self.c.execute('SELECT DISTINCT ComLib FROM installation')
		return results

	def afficheInstallationParVille(self, ville):
		results = self.c.execute('''SELECT DISTINCT InsPartLibelle FROM installation WHERE ComLib = "'''+ ville +'''"''')
		return results

	def commit(self):
		self.conn.commit()