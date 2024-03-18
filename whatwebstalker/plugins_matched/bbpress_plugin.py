import plugins
			
class Pluginbbpress_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name="generator" content="bbPress ([\d\.]+)" \/>/" },
			{ "regexp" : "/ is proudly powered by <a[^>]+href="http:\/\/bbpress\.org">bbPress<\/a>/" },
			{ "text" : "<!-- If you like showing off the fact that your server rocks -->" },
			{ "text" : "<div id="bbpress-forums">" },
		]
		return(self.rules)
