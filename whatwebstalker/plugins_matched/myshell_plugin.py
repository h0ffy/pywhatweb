import plugins
			
class Pluginmyshell_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "&nbsp;| ::::::::::&nbsp;<a href="http://www.digitart.net" target="_blank" style="text-decoration:none"><b>MyShell</b> &copy;2001 Digitart Producciones</a>" },
			{ "version" : "/<title>MyShell ([\d\.]+ build [\d]{8})<\/title>/" },
		]
		return(self.rules)
