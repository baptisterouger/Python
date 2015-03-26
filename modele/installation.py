class Installation:
    def __init__(self, InsNumeroInstall, InsPartLibelle, InsNoVoie, InsLibelleVoie, InsCodePostal, ComLib, Latitude, Longitude):
        self.InsNumeroInstall = InsNumeroInstall
        self.InsPartLibelle = InsPartLibelle
        self.InsNoVoie = InsNoVoie 
        self.InsLibelleVoie = InsLibelleVoie
        self.InsCodePostal = InsCodePostal
        self.ComLib = ComLib
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.InsNumeroInstall = InsNumeroInstall
        


    def __repr__(self):
        return "{} - {}".format(self.InsNumeroInstall, self.InsPartLibelle)
    
    def get_InsNumeroInstall(self):
    	return str(self.InsNumeroInstall)
    def get_InsPartLibelle(self):
    	return str(self.InsPartLibelle)
    def get_adresse(self):
    	return str(self.InsNoVoie +" "+ self.InsLibelleVoie)
    def get_InsNoVoie(self):
        return str(self.InsNoVoie)
    def get_InsLibelleVoie(self):
        return str(self.InsLibelleVoie)
    def get_InsCodePostal(self):
    	return str(self.InsCodePostal)
    def get_ComLib(self):
    	return str(self.ComLib)
    def get_Latitude(self):
    	return str(self.Latitude)
    def get_Longitude(self):
    	return str(self.Longitude)

    def set_InsNumeroInstall(self, t):
    	self.InsNumeroInstall = t
    def set_InsPartLibelle(self, t):
    	self.InsPartLibelle = t
    def set_adresse(self, t):
    	self.adresse = t
    def set_InsCodePostal(self, t):
    	self.InsCodePostal = t
    def set_ComLib(self, t):
    	self.ComLib = t
    def set_Latitude(self, t):
    	self.Latitude = t
    def set_Longitude(self, t):
    	self.Longitude = t