import plugins
			
class Plugini3micro_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "model" : "'VRG", "url" : "/favicon.ico", "md5" : "e4a509e78afca846cd0e6c0672797de5" },
			{ "model" : "/^Digest realm="i3micro (V[A-Z]{2})", "nonce/", "search" : "headers[www-authenticate]" },
		]
		return(self.rules)
