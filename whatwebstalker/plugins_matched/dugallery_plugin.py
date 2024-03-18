import plugins
			
class Plugindugallery_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "ghdb" : "ext:asp inurl:DUgallery intitle:"3.0"", "version" : "3.0", "certainty" : "75 },
			{ "regexp" : "/<title>DUgallery[^<]*<\/title>/" },
			{ "text" : "<img src="assets/title.gif" alt="Powered by DUportal" width="269" height="62" border="0">" },
			{ "version" : "/<title>DUgallery ([\d\.]+)<\/title>/" },
		]
		return(self.rules)
