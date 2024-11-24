import plugins


class Pluginzope_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"search": "headers[server]", "version": "/Zope\\/\\(([^,]*)/"},
			{"search": "headers[server]", "module": / Zope\/\([^,]*", "([^,]*)/" },
			{ "search" : "headers[server]", "string" : /Zope\/\([^,]*", "[^,]*", "([^\)^\s]*)/" },
		]
	return(self.rules)
