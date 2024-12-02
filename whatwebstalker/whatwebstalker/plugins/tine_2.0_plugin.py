import plugins


class Plugintine_2.0_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- Tine 2.0 static files -->" },
			{ "text" : "<!-- Tine 2.0 setup static files -->" },
			{ "text" : "Powered by: <a target="_blank" href="http://www.tine20.org/">Tine 2.0</a></div>" },
			{ "text" : "<noscript><p>You need to enable javascript to use <a href="http://www.tine20.org/" title="online open source groupware and crm">Tine 2.0</a></p></noscript>" },
			{ "text" : "<noscript>You need to enable javascript to use <a href="http://www.tine20.org">Tine 2.0 setup or use the CLI setup</a></noscript>" },
		]
	return(self.rules)
