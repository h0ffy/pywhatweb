import plugins
			
class Pluginyoutube_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<(param|embed) [^>]*youtube\.com\/v/i },
			{ "regexp" : "/<iframe [^>]*src=['"]https?:\/\/(www\.)?youtube\.com\/embed\//" },
		]
		return(self.rules)
