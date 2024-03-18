import plugins
			
class Pluginkolab_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "md5" : "8b2a22d60ef1352abd1e2e35f711bbf7", "url" : "/favicon.png" },
			{ "text" : "<div id="toptitle">Kolab Groupware login</div>" },
			{ "text" : "<meta name="description" content="Kolab Administration Webinterface" />" },
			{ "text" : "<title>Kolab Groupware login</title>" },
		]
		return(self.rules)
