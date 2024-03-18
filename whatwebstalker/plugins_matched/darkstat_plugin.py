import plugins
			
class Plugindarkstat_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<li class="label">darkstat ([^\s^<]+)<\/li><li><a href="[^"]+">graphs<\/a><\/li>/" },
			{ "version" : "/<title>darkstat ([^\s]+) : graphs ([^\s^\)]+)<\/title>/" },
			{ "search" : "headers[server]", "version" : "/^darkstat\/([^\s]+)$/" },
		]
		return(self.rules)
