import cherrypy
import json
 
 
data = json.loads(open("BDInstall.json").read())
 
 
class WebManager(object):


	def index(self):

		return "There are {0} items".format(len(data))

	def show_all(self):

		return json.dumps(data)
	 

	def show(self, id):

		try:
			item = data[int(id)]
		except (IndexError, IOError):
			return "Invalid ID"
			 
		return json.dumps(item)
	 
 
cherrypy.quickstart(WebManager()) 
