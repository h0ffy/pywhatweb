import plugins
			
class Pluginreinvigorate_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "10", "text" : "<!-- Reinvigorate -->" },
			{ "text" : "<script type="text/javascript" src="http://include.reinvigorate.net/re_.js"></script>" },
			{ "certainty" : "25", "string" : /reinvigorate\.track\("([a-z\d]{5}-[a-z\d]{10})"\);/" },
			{ "certainty" : "10", "string" : /re_\("([a-z\d]{5}-[a-z\d]{10})"\);/" },
		]
		return(self.rules)
