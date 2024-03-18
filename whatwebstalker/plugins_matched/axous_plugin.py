import plugins
			
class Pluginaxous_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "regexp" : "/<meta name="generator" content="Axous V([^"]+)" \/>/" },
			{ "version" : "/Powered by <a href="http:\/\/www\.axous\.com\/" target="_blank" title="Axous Shareware Shop">Axous ([^\s]+)<\/a> &copy;/" },
			{ "text" : "<div class="tit2 tit3">Products</div>" },
		]
		return(self.rules)
