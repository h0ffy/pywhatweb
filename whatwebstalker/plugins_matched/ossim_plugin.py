import plugins
			
class Pluginossim_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title> AlienVault - Open Source SIM </title>" },
			{ "text" : "<table align="center" style="padding:1px;background-color:#f2f2f2;border-color:#aaaaaa" class=nobborder><tr><td class="nobborder">" },
			{ "text" : "<table align="center" cellspacing=4 cellpadding=2 style="background-color:#eeeeee;border-color:#dedede">" },
		]
			return(self.rules)
