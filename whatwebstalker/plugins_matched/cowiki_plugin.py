import plugins
			
class Plugincowiki_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<!-- Generated by coWiki ([^ ]+) \((http:\/\/www.develnet.org|http:\/\/www.cowiki.org)\) -->/" },
			{ "version" : "/<meta name="generator" content="coWiki ([^,]+)", "(http:\/\/www.develnet.org|http:\/\/www.cowiki.org)"[^>]*>/" },
		]
	return(self.rules)

