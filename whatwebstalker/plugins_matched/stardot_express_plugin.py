import plugins
			
class Pluginstardot_express_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "%r{<title>Express6 Live Image( Popup)?</title>}", "version" : "'6" },
			{ "regexp" : "%r{<tr><td><a href="http://www.stardot(-tech)?.com" target="(_new|_blank)"><img src="logo.gif" alt=" width="227" height="45"} },
			{ "status" : "401", "certainty" : "75", "name" : "WWW-Authenticate realm", "regexp" : "/^Basic realm="Express6"/", "search" : "headers[www-authenticate]" },
		]
		return(self.rules)
