import plugins
			
class Pluginoki_pbx_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>IPstageMaintenanceConsole(PBX)</title>" },
			{ "text" : "<APPLET CODE="DavisBar.class" ARCHIVE="ipstage.jar"" },
			{ "text" : "<PARAM NAME="systype"    value="OKI">" },
		]
	return(self.rules)
