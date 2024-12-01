import plugins
			
class Plugintrident7_wave7_olt_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<TITLE>Trident7 System Login</TITLE>" },
			{ "string" : /<TD VALIGN="bottom" COLSPAN=2><FONT SIZE=2 ALIGN="justify">&copy; (20[\d]{2}) Wave7 Optics", "Inc\. All rights reserved\./" },
		]
	return(self.rules)
