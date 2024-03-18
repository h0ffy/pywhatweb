import plugins
			
class Pluginsendcard_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a href="http:\/\/(sendcard.sf.net|www.sendcard.org)\/"( title="download your own PHP e-card script")?><img src="poweredbysendcard102x47.gif"[^>]+alt="Powered by sendcard - an advanced PHP e-card program"[^>]*><\/a>/" },
			{ "certainty" : "25", "regexp" : "/<img src="poweredbysendcard102x47.gif"[^>]+alt="Powered by sendcard - an advanced PHP e-card program">/" },
			{ "text" : "<!-- The following line should allow me to search on google and find sendcard installations -->" },
			{ "text" : "<div style="display: none; color: White;">scscsc320</div>" },
		]
		return(self.rules)
