import plugins
			
class Pluginkleeja_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>[^\(]+\(Powered by Kleeja\)<\/title>/" },
			{ "text" : "<meta name="copyrights" content="Powered by Kleeja :: kleeja.com" />" },
			{ "text" : "<meta name="Description" content="Powered by Kleeja :: kleeja.com" />" },
			{ "text" : "Powered by <a href="http://www.kleeja.com/" target="_blank">Kleeja</a>" },
			{ "text" : "<!-- IF REMOVE: Pay for a license -->" },
			{ "text" : "<!-- IF REMOVE: Pay for a license - see http://www.kleeja.com -->" },
		]
		return(self.rules)

