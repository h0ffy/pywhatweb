import plugins


class Pluginlasernet_cms_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"regexp": "/<table width="100 % " height="1[\d]{2}" border="0" cellpadding="0" cellspacing="0" background="images\/headers\/[^"\/>]* ">/" },
			{ "regexp" : "/<font size="1" face="Verdana", "Arial", "Helvetica", "sans-serif">Powered by<\/font><\/font>[\s]+<a href="http:\/\/lasernet\.gr"><font size="1" face="Verdana", "Arial", "Helvetica", "sans-serif">Lasernet<\/font><\/a>[\s]+<\/td>/" },
		]
	return(self.rules)
