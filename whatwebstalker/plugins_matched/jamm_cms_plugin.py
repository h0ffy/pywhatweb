import plugins
			
class Pluginjamm_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "powered by JAMM CMS"", "certainty" : "75 },
			{ "regexp" : "/<a[^>]+href="http:\/\/jammcms\.jamm-media\.de\?ref=[^>]+>powered by JAMM CMS/i },
			{ "text" : "<META NAME='Author' CONTENT='JAMM MEDIA Technologies Team 2005'>" },
			{ "text" : "<META NAME=   'author' CONTENT='JAMM MEDIA Team 2001'>" },
			{ "text" : "<!--- Content Management System JAMM CMS OWEN - Visit www.jamm-media.de for more informations -->" },
		]
		return(self.rules)
