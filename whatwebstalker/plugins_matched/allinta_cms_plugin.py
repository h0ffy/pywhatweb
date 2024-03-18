import plugins
			
class Pluginallinta_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/	<link rel="stylesheet" href="css\/wizard\/t[0-9_]+.css" type="text\/css">/" },
			{ "regexp" : "/	<link href="css\/wizard\/t[0-9_]+.css" rel="stylesheet" type="text\/css">/" },
			{ "text" : "		<td align="right" class="footerText">Powered by allinta CMS</td>" },
			{ "regexp" : "/<img src="img\/wizard\/t[0-9_]+\/powered_allinta.gif"[^>]*alt="Powered by Allinta CMS"/" },
			{ "regexp" : "/<img contenteditable="inherit" start="fileopen" height="[0-9]+" src="img\/powered_allinta.gif" width="[0-9]+" \/>/" },
			{ "text" : "<title>allinta.com- aCMS Content Manager</title>" },
			{ "version" : "/<!-- allintaCMS V([\d\.]+) - http:\/\/www.allinta.com\/ -->/" },
		]
			return(self.rules)
