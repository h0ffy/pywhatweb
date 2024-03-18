import plugins
			
class Pluginblogsmithmedia_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "regexp" : "/<script [^>]*\"http:\/\/www.blogsmithmedia.com},
		]
	return(self.rules)

