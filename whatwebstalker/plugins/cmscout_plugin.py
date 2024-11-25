import plugins
			
class Plugincmscout_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered by CMScout &copy;[\d\,]+ <a href="http:\/\/www.cmscout.za.net" title="CMScout Group" target="_blank">CMScout Group<\/a>/" },
			{ "text" : "<!--Shows the CMScout and website copyright information. Please do not remove this without permission from the CMScout admin-->" },
		]
	return(self.rules)
