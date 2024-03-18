import plugins
			
class Pluginuniform_server_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<div id="divider">Developed By <a href="http://www.uniformserver.com/">The Uniform Server Development Team</a></div>" },
			{ "text" : "<meta name="Description" content="The Uniform Server 8.1.0-Coral." />" },
			{ "version" : "/<p style=" font-size:24px; margin: 0px; padding-top:10px">\s+The Uniform Server <br \/>\s+([^\s]+)\s+<\/p>/" },
			{ "text" : "<div id="header"><a href="http://www.uniformserver.com"><img src="images/logo.jpg" align="left" alt="The Uniform Server" /></a>" },
		]
	return(self.rules)
