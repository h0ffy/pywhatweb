import plugins
			
class Pluginsitegenius_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "ghdb" : "inurl:"sitegenius/topic.php"" },
			{ "regexp" : "/var PortalBrowser = window.open\('popup.php\?page_type='\+page_type\+'&lang=[A-Z]{2}&page_id='\+pgid(\+addToURL)?", "'", "myFeatures\); /" },
		]
		return(self.rules)
