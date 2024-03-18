import plugins
			
class Plugingcards_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<a href="compose.php?imageid=" },
			{ "text" : "<title>eCards Administration Console Login</title>" },
			{ "version" : "/<td>(Driftet av|Powered by|Un script de ) <a href="http:\/\/www.gregphoto.net\/gcards\/index.php"[^>]*>gCards<\/a> v([\d\.]+)<\/td>/", "offset" : "1 },
		]
	return(self.rules)

