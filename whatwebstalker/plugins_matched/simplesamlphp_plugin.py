import plugins
			
class Pluginsimplesamlphp_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>simpleSAMLphp installation page</title>" },
			{ "regexp" : "/<h1><a style="text-decoration: none; color: white" href="[^"]+">simpleSAMLphp installation page<\/a><\/h1>/" },
			{ "text" : "<a href="http://rnd.feide.no/simplesamlphp">SimpleSAMLPhp </a>" },
			{ "certainty" : "75", "text" : "<!-- Grey header bar below -->" },
		]
		return(self.rules)
