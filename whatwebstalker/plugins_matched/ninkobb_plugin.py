import plugins
			
class Pluginninkobb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<link href="[^"]*\/assets\/css\/ninko.css" rel="stylesheet" type="text\/css" \/>/" },
			{ "text" : "Powered by <a href="http://ninkobb.com">NinkoBB</a>" },
			{ "version" : "/Powered by <a href="http:\/\/ninkobb.com\/">NinkoBB<\/a> v. ([\d\.]{1,5}) t./" },
		]
	return(self.rules)
