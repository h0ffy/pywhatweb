import plugins
			
class Pluginyamamah_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<p>Copyright &copy; [\d]{4}  All rights reserved. Powered By : <a href="http:\/\/www.yamamah.org" title="Yamamah">Yamamah Version ([\d\.]{1,5})<\/a><\/p>/" },
			{ "text" : "<meta name="Author" content="Majed Al-Mulihani - majed@modernsys.net" />" },
			{ "text" : "<meta name="Description" content="Yamamah is free photo gallery cms" />" },
		]
		return(self.rules)
