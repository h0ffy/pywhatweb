import plugins
			
class Pluginmjniohttpdaemon_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^MJNioHttpDaemon\/([^\s]+)/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/MJNIOHTTPDSESSIONID=/" },
		]
			return(self.rules)
