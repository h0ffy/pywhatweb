import plugins
			
class Pluginseagate_goflex_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[location]", "string" : /^https:\/\/www\.seagateshare\.com\/\?hipname=([^\s^&]+)/" },
			{ "string" : /<input id="inSubdomain" name="inSubdomain" type="text" maxlength="30" size="23" value="([^\s^"^>]*)"><br><br>/" },
		]
	return(self.rules)

