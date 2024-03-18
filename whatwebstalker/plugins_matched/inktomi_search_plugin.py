import plugins
			
class Plugininktomi_search_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "search" : "headers[server]", "version" : "/^Inktomi Search ([^\s]+)$/" },
			{ "url" : "/util/badkey.html", "version" : "/<font size="\+1"><b>License Key Problems<\/b><\/font><br>[\s]+<b>Inktomi Search ([^<^\s]+)<\/b><br>/" },
		]
		return(self.rules)

