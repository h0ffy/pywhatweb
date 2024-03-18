import plugins
			
class Plugincruxcms_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<font color="#666666"><center>Powered by <a href="http://www.cruxcms.co.uk">Crux CMS</a></center> </font>" },
			{ "text" : "<font color="#666666"><center>Powered by <a href="http://www.cruxsoftware.co.uk">Crux CMS</a></center> </font>" },
			{ "text" : "<meta name="Generator" content="Created by CruxCMS http://www.cruxsoftware.co.uk">" },
			{ "text" : "<meta name="Generator" content="Created by Crux CMS http://www.cruxcms.co.uk">" },
		]
	return(self.rules)
