import plugins
			
class Pluginsmodcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="Generator" content="SmodCMS" />" },
			{ "text" : "<meta name="Authoring_Tool" content="SmodCMS // www.smod.pl" />" },
			{ "regexp" : "/[P|p]+owered by <a href="http:\/\/www.smod.pl[\/]+"[^>]+>SmodCMS[\s]*<\/a>/" },
		]
			return(self.rules)
