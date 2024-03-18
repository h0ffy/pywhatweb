import plugins
			
class Pluginpixelpost_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/[Pp]owered by <a href="http:\/\/www.pixelpost.org[\/]?"[\s]*(title="Powered by Pixelpost")?>[Pp]ixel[Pp]ost</" },
			{ "text" : "Powered by <a onclick="window.open(this.href); return false;" href="http://pixelpost.org/" title="Pixelpost">Pixelpost</a>" },
		]
			return(self.rules)
