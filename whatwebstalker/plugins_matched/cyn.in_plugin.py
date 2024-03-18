import plugins
			
class Plugincyn.in_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<meta name="generator" content="cyn.in - http://cyn.in" />" },
			{ "md5" : "3640b38549e4eeb872f66ec53ee27842", "url" : "/favicon.ico" },
			{ "version" : "/<a href="http:\/\/www\.cynapse\.com\/cynin" target="_blank" class="smallcolophonmainlink">Powered by cyn\.in v([^\s]+) - free open source edition<\/a>/" },
		]
		return(self.rules)
