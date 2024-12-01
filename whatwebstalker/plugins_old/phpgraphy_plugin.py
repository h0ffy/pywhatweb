import plugins
			
class Pluginphpgraphy_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<title>my phpGraphy site</title>" },
			{ "version" : "/This site is using <a href="http:\/\/phpgraphy\.sourceforge\.net\/">phpGraphy<\/a>\n([^\s]+) - Page generated in [\d\.]+s\.<\/div><!--\/\/footer-->/" },
		]
	return(self.rules)
