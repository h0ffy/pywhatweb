import plugins
			
class Plugindiferior_cms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "&#8212; Powered by Diferior</title>" },
			{ "regexp" : "/<a href="http:\/\/diferior.com" rel="external_dif[^>]+>Powered by Diferior", "Copyright &copy; 2007", "2008 Povilas Musteikis<\/a><br\/>/" },
		]
		return(self.rules)
