import plugins
			
class Pluginepiware_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div id="masthead"><a href="http:\/\/www\.epiware\.com">Epiware<\/a><\/div>\s+<span class="version">version ([^<^\s]+)<\/span>/" },
			{ "text" : "<title>Epiware - Project and Document Management  </title>" },
			{ "regexp" : "/<div id="jsWarning" class="javascript_warning">\s+This web-site requires javascript\.\s+Please enable javascript to access this web-site\.\s+<\/div>/" },
		]
	return(self.rules)
