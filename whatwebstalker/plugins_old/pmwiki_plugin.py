import plugins
			
class Pluginpmwiki_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[set-cookie]", "regexp" : "/imstime=[\d]+;/" },
			{ "text" : "<!--PageLeftFmt-->" },
			{ "text" : "<span class='commentout-pmwikiorg'>" },
			{ "regexp" : "/<link rel='stylesheet' href='[^']*\/pmwiki\/pub\/skins\/pmwiki\/pmwiki\.css' type='text\/css' \/>/" },
		]
	return(self.rules)
