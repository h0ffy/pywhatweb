import plugins
			
class Plugintoshiba_printer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE CLASS="clsTitle1">TopAccess</title>" },
		]
	return(self.rules)
