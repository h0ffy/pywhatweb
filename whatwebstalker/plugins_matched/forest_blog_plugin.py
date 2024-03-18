import plugins
			
class Pluginforest_blog_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/Powered [B|b]?y[:]? <a href="http:\/\/www.hostforest.co.uk\/[^"]*"[^>]+title="Forest Blog"[^>]*>/" },
			{ "text" : "<title>Forest Blog Administration</title>" },
			{ "text" : "			<h1>Forest Blog Administration</h1>" },
			{ "version" : "/Powered [B|b]?y[:]? <a href="http:\/\/www.hostforest.co.uk\/[^"]*"[^>]+title="Forest Blog"[^>]*>Forest Blog<\/a> v([\d\.]+)/" },
		]
	return(self.rules)

