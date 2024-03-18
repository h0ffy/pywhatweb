import plugins
			
class Pluginmobotix_network_camera_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="publisher" content="MOBOTIX AG", "Germany">" },
			{ "text" : "<meta name="copyright" content="MOBOTIX AG", "Germany">" },
			{ "text" : "<meta name="author" content="Daniel Kabs", "MOBOTIX AG", "Kaiserslautern", "Germany.">" },
			{ "regexp" : "/<font face="Helvetica,Arial" size="-2">	&copy;2001[\-0-9]{0,5} <a href="\/about.html">MOBOTIX AG<\/a>", "Germany  &middot; <a href="http:\/\/www.mobotix.com\/">http:\/\/www.mobotix.com\/<\/a>/" },
			{ "firmware" : "/var filesystem__version="[M0-1\-]*V([\d\.]+)";/" },
		]
	return(self.rules)

