import sqlite3

conn = sqlite3.connect('installation.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS installation")
c.execute('''CREATE TABLE installation
             (InsNumeroInstall integer, InsPartLibelle text, InsNoVoie integer, InsLibelleVoie text, InsCodePostal integer, ComLib text, Latitude integer, Longitude integer)''')

conn.commit()
conn.close()

conn = sqlite3.connect('equipement.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS equipement")
c.execute('''CREATE TABLE equipement
             (EquipementId integer, EquNom text, InsNumeroInstall integer)''')

conn.commit()
conn.close()

conn = sqlite3.connect('activite.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS activite")
c.execute('''CREATE TABLE activite
             (ActCode integer, ActLib text, EquipementId integer)''')

conn.commit()
conn.close()