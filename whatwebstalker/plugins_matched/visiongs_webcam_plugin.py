import plugins
			
class Pluginvisiongs_webcam_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>VisionGS Webcam Software</title>" },
			{ "text" : "  <!-- VisionGS Still Code Begin -->" },
			{ "regexp" : "/<a href="http:\/\/www.visiongs.de\/"><font [size="1"\ ]*face="Verdana", "Arial", "Helvetica", "sans-serif"[\ size="1"]*>VisionGS/" },
		]
		return(self.rules)
