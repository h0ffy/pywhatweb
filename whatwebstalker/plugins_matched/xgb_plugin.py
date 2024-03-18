import plugins
			
class Pluginxgb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "	<title>xGB</title>" },
			{ "text" : "<!-- start xGB dynamic content -->" },
			{ "text" : "powered by <a href='http://www.x-gfx.de' target='blank' title='Script by x-gfx.de'>xGB" },
			{ "version" : "/<p align='center'><span id='copyright'>\[ powered by <a href='http:\/\/www.x-gfx.de' target='blank' title='Script by x-gfx.de'>xGB ([\d\.]+)<\/a>/" },
		]
		return(self.rules)

