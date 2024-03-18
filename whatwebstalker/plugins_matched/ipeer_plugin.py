import plugins
			
class Pluginipeer_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<title>iPeer V(\d) with TeamMaker<\/title>/" },
			{ "text" : "<h1 align="center"><span class="footer">Powered by iPeer and TeamMaker - Created by UBC and Rose-Hulman</span></h1>" },
			{ "version" : "/<span class="bannerText"><span style='font-size: 120%;'>([^<]+)<\/span>&nbsp;&nbsp;with TeamMaker<\/span><\/td>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/IPEER=[^;]+;/" },
		]
		return(self.rules)
