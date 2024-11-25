import plugins
			
class Pluginphpdocumentor_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "certainty" : "75", "text" : "<title>docBuilder - phpDocumentor web interface</title>" },
			{ "text" : "<meta name="Description" content="Frameset for phpDcoumentor docBuilder web interface">" },
			{ "text" : "<meta name="Description" content="Frameset for phpDocumentor docBuilder web interface">" },
			{ "filepath" : "/<input type="text" name="fileName" value="([^"]+)" size="60" class="text" \/>/" },
			{ "version" : "/	<title>\n		Form to submit to phpDocumentor v([^\s]+)	<\/title>/" },
			{ "version" : "/<span class="title"><strong>docBuilder<\/strong> :: phpDocumentor v([^\s]+) Web Interface<\/span>/" },
		]
	return(self.rules)
