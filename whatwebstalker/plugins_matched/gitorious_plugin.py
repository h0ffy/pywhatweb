import plugins
			
class Plugingitorious_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<a href="http:\/\/gitorious\.org"><img alt="Poweredby" src="\/images\/\.\.\/img\/poweredby\.png\?[\d]+" title="Powered by Gitorious" \/><\/a><\/div>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/_gitorious_sess=[^-]+--[^;]+; domain=/" },
		]
		return(self.rules)
