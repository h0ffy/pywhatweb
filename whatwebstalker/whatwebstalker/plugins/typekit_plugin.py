import plugins


class Plugintypekit_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/<script [^>]*src=["'][^>]*use\.typekit\.com/i },
		]
	return(self.rules)
