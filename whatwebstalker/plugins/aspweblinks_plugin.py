import plugins
			
class Pluginaspweblinks_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/Powered By aspWebLinks ([\d\.]+) from <A[^>]*HREF=["']http:\/\/www.fullrevolution.com[^>]*>Full Revolution", "Inc.<\/A>/" },
			{ "version" : "/<A[^>]*HREF=["']http:\/\/www.fullrevolution.com[^>]*>Powered By aspWebLinks ([\d\.]+)<\/A>/" },
			{ "version" : "/<title>aspWebLinks ([\d\.]+)<\/title>/" },
		]
	return(self.rules)
