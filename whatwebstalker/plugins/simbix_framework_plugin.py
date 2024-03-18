import plugins
			
class Pluginsimbix_framework_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "url" : "logo-lpage-owner.png", "md5" : "500cf2101e7b3512f602203695726520" },
			{ "text" : "<div class="image"><img src="/logo-lpage.png" width="40" height="40" alt="Simbix Framework" /></div>" },
			{ "version" : "/<meta name="generator" content="Simbix Framework v([^"^\s]+)" \/>/" },
		]
	return(self.rules)
