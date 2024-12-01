import plugins
			
class Pluginxchangeboard_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "h1,h2,h3,h4,p,ul,ol,li,div,td,th,address,blockquote,nobr,b,i {" },
			{ "version" : "/	<div align="center"><small>Powered by <a href="http:\/\/www.xchangeboard.de">XchangeBoard<\/a> ver ([\d\.a-z]+) - /" },
		]
	return(self.rules)
