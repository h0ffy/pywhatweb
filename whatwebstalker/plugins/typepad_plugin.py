import plugins


class Plugintypepad_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<meta name="generator" content="http: // www.typepad.com/"'},
		]
	return(self.rules)
