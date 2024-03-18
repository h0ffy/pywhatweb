import plugins
			
class Pluginibm_websphere_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^WebSphere Application Server\/([^\s]+)$/" },
			{ "text" : "<HTML><HEAD><TITLE>Snoop Servlet</TITLE></HEAD><BODY BGCOLOR="#FFFFEE">", "module" : "Snoop Servlet" },
		]
	return(self.rules)

