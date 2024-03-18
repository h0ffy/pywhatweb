import plugins
			
class Pluginnetsnap_web_camera_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Live NetSnap Cam-Server feed</title>" },
			{ "text" : "color="#008080">Live-Webcam</font></big></big></big></strong></em></font></h3>" },
			{ "text" : "color="#008080">NetSnap®</font></big></big></big></big><font size="6"> </font></strong></font></em></h3>" },
			{ "text" : "<p align="center"><font face="Arial"><small><small>NetSnap is a registered Trademark of" },
		]
		return(self.rules)
