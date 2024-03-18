import plugins
			
class Pluginnetvehicle_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<HEAD><TITLE>Welcome to NetVehicle</TITLE></HEAD>" },
			{ "url" : "/nv_logo.gif", "md5" : "efff3142fb8f4e34836ca5b38ca40512" },
			{ "regexp" : "/^NetVehicle/", "search" : "headers[server]" },
			{ "model" : "/^NetVehicle-([A-Z\d]{1,3})/", "search" : "headers[server]" },
		]
		return(self.rules)
