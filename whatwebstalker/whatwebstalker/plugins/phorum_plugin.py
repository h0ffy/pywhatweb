import plugins


class Pluginphorum_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/powered by <a href="http: \/\/www\.phorum\.org\/"( target="_blank")?>Phorum<\/a>\./" },
			{ "certainty" : "75", "text" : "<!-- end of div id=user-info -->" },
		]
	return(self.rules)
