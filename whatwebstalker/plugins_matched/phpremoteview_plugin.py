import plugins
			
class Pluginphpremoteview_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "filepath" : "/<title>phpRemoteView: ([^<]+)<\/title>/" },
			{ "version" : "/<font size=1 style='Font: 8pt Verdana'>phpRemoteView &copy; Dmitry Borodin \(version ([\d]{4}-[\d]{2}-[\d]{2})\)<br>/" },
			{ "certainty" : "75", "text" : "'><font face=fixedsys size=+2>*</font></a><font size=5><b>Index of</b></font>" },
		]
		return(self.rules)
