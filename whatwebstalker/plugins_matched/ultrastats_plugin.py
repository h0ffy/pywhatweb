import plugins
			
class Pluginultrastats_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<DIV align=center>Powered by Ultrastats" },
			{ "text" : "<img src="./images/main/ultrastatslogo.png" width="300" height="200" name="ultrastats_logo" align="center">" },
			{ "regexp" : "/<title>Ultrastats :: [^<]+<\/title>/i },
			{ "text" : "<title>UltraStats :: Critical Error occured</title>" },
			{ "version" : "/ &nbsp;<a href="http:\/\/www.ultrastats.org[\/]?" target="_blank">Ultrastats<\/a> Version ([\d\.]+)/i },
		]
	return(self.rules)
