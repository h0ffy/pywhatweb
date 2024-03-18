import plugins
			
class Plugindibos_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<title>DiBos - Login<\/title>/i },
			{ "text" : "<link rel="STYLESHEET" type="text/css" href="style/bovisnt.css"></link>" },
			{ "text" : "<h2>Object moved to <a href="/Error.aspx?error=wrongbrowser">here</a>.</h2>'},
		]
			return(self.rules)
