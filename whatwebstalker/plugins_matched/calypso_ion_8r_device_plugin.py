import plugins
			
class Plugincalypso_ion_8r_device_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<title>Calypso ION-8r Device</title>" },
			{ "text" : "<li><a href="/A/cfg/entercmd.stm">Enter Command</a></li>" },
			{ "search" : "headers[www-authenticate]", "text" : "Calypso ION8r Device" },
		]
		return(self.rules)
