class Equipement :
	def __init__(self, EquipementId, EquNom, InsNumeroInstall):
		self.EquipementId = EquipementId
		self.EquNom = EquNom
		self.InsNumeroInstall = InsNumeroInstall

	def __repr__(self):
		return "{} - {}".format(self.EquipementId, self.EquNom)

	def display_EquipementId(self):
		return str(self.EquipementId)
	def display_EquNom(self):
		return str(self.EquNom)
	def display_InsNumeroInstall(self):
		return str(self.InsNumeroInstall)

	def set_EquipementId(self, t):
		self.EquipementId = t
	def set_EquNom(self, t):
		self.EquNom = t
	def set_InsNumeroInstall(self, t):
		self.InsNumeroInstall = t