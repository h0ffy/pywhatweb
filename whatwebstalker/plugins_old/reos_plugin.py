import plugins
			
class Pluginreos_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "Powered by <a href="http://reos.elazos.com">ReOS</a>" },
			{ "version" : "/Powered by <a href="http:\/\/reos.elazos.com">ReOS ([\d\.]+)<\/a> and released under the <a href="http:\/\/www.fsf.org\/licensing\/licenses\/agpl\-3\.0\.html">GNU\/AGPLv3 License.<\/a>/" },
			{ "version" : "/Powered by <a href="http:\/\/reos.elazos.com">ReOS ([\d\.]+)<\/a> and released under the <a href="http:\/\/creativecommons.org\/licenses\/GPL\/2.0\/">GNU\/GPL License.<\/a>/" },
		]
	return(self.rules)
