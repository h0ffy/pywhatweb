import plugins
			
class Pluginopendocman_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<a href="http:\/\/www\.opendocman\.com\/" target="_new">OpenDocMan v([^"^\s]+)<\/a>/" },
			{ "text" : "<td align="left"><img src="images/logo.gif" alt="Site Logo" border=0></td>" },
			{ "regexp" : "/<td valign="top">\s+Welcome to OpenDocMan\.?\s+<p>/" },
		]
	return(self.rules)
