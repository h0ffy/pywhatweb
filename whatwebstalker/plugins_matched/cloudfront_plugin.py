import plugins
			
class Plugincloudfront_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "status" : "403", "text" : "<html><body>Sorry", "invalid request</body></html>" },
			{ "search" : "headers[server]", "regexp" : "/^CloudFront/" },
			{ "search" : "headers[x-cache]", "regexp" : "/^Error from cloudfront/" },
		]
		return(self.rules)
