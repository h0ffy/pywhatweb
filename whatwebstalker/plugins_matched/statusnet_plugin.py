import plugins
			
class Pluginstatusnet_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<p>This site is powered by <a href="http:\/\/status\.net\/">StatusNet<\/a> version ([^\s]+),/" },
			{ "version" : "/It runs the <a href="http:\/\/status\.net\/">StatusNet<\/a> microblogging software", "version ([^\s]+)", "available under the <a /" },
		]
		return(self.rules)

