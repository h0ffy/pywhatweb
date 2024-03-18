import plugins
			
class Plugincervis_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<a href="http://www.cervistech.com" target="_blank"><img src="/acts/images/cervis_logo_sm.png" align=\'absmiddle\' border="0" />Powered by CERVIS</a>" },
			{ "string" : /<meta name="title" content="(Volunteer)? Opportunities and Event Registration ([^"]+)" \/>/", "offset" : "1 },
		]
		return(self.rules)
