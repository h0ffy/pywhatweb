import plugins
			
class Plugins_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<p class="alignRight">Powered by S:CMS - Copyright ©" },
			{ "text" : "<title>SCMS</title>" },
			{ "text" : "<!-- Inizio righe di indicizzazione nei motori di ricerca -->" },
			{ "version" : "/Powered by <a href='http:\/\/www.matteoiammarrone.com\/public\/s-cms' target='_blank'>S-Cms ([\d\.]+)<\/a>/" },
		]
	return(self.rules)

