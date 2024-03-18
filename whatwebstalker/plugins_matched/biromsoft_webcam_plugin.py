import plugins
			
class Pluginbiromsoft_webcam_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Biromsoft WebCam</title>", "certainty" : "75 },
			{ "regexp" : "/<area shape="rect" coords="[\d\-,]+" href="http:\/\/www.biromsoft.com" alt="Visit BiromSoft " title="Visit BiromSoft ">/" },
			{ "text" : "<area shape="rect" coords="22,26,151,102" href="http://www.biromsoft.com">" },
		]
		return(self.rules)
