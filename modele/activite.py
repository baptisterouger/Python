class Activite :
	def __init__(self, ActCode, ActLib, EquipementId):
		self.ActCode = ActCode
		self.ActLib = ActLib
		self.EquipementId = EquipementId

	def __repr__(self):
		return "{} - {}".format(self.ActCode, self.ActLib)
    
	def display_ActCode(self):
		return str(self.ActCode)
	def display_ActLib(self):
		return str(self.ActLib)
	def display_EquipementId(self):
		return str(self.EquipementId)

	def set_ActCode(self, t):
		self.ActCode = t
	def set_ActLib(self, t):
		self.ActLib = t
	def set_EquipementId(self, t):
		self.EquipementId = t