import plugins


class Pluginspeedtouch_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"url": "/favicon.ico", "md5": "befcded36aec1e59ea624582fcb3225c"},
			{"regexp": "/(Basic|Digest) realm="SpeedTouch / ", "search" : "headers[www - authenticate]", "name" : "WWW - Authenticate realm" },
		]
	return(self.rules)
