import plugins
			
class Plugindell_printer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "/<title>Dell Laser Printer ([A-Z]?[\d]{4}[a-z]{0,2})<\/title>/i },
			{ "model" : "/<TITLE>Dell ([\d]{4}[a-z]+) Laser Printer<\/TITLE>/" },
		]
	return(self.rules)
