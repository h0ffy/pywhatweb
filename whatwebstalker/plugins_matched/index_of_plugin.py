import plugins
			
class Pluginindex_of_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>Index of /" },
			{ "certainty" : "75", "ghdb" : "name "last modified" size description" },
			{ "text" : "<a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a>" },
			{ "regexp" : "/<a href="\?C=N;O=D">Name<\/a>[\s]*<a href="\?C=M;O=A">Last modified<\/a>/" },
			{ "regexp" : "/<pre>Name[\s]+Last modified[\s]+Size[\s]+<hr>/" },
			{ "regexp" : "/<A HREF="\?N=D">Name<\/A>[\s]+<A HREF="\?M=A">Last modified<\/A>/" },
		]
		return(self.rules)
