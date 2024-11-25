import plugins
			
class Pluginorbis_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="description" content="Orbis CMS is a simple and stylish management solution for small websites." />" },
			{ "text" : "<div id="login_poweredby">Powered by Orbis CMS</div>" },
			{ "text" : "<title>Orbis CMS &gt; Login</title>" },
			{ "text" : "<!-- Give feedback if user enters incorrect password (GET value "e=2) or logged out (GET value "e=3") -->" },
		]
	return(self.rules)
