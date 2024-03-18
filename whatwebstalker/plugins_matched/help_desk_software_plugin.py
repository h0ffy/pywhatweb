import plugins
			
class Pluginhelp_desk_software_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<div class="AdminTDSmall">[\s]+powered by <a href="http:\/\/freehelpdesk\.org\/\?ver=([^"^>^\s]+)" target="_blank">freehelpdesk\.org<\/a>[\s]+<\/div>/" },
			{ "version" : "/<\/html>[\s]+<font style='font-size:0px'>([^<^\s]+)<\/font>/" },
		]
		return(self.rules)
