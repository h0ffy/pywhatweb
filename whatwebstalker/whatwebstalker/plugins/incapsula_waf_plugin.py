import plugins


class Pluginincapsula_waf_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"name": "Set-cookie Header", "search": "headers[set-cookie]", "regexp": "/incap_ses_/i},
			{ "name" : "Set-cookie Header", "search" : "headers[set-cookie]", "regexp" : "/incap_visid_83_/i},
			{ "name" : "visid_incap_ cookie", "search" : "headers[set-cookie]", "regexp" : "/^visid_incap_/" },
		]
	return(self.rules)
