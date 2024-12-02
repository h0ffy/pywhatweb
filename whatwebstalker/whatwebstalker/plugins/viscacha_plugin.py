import plugins


class Pluginviscacha_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<meta name="generator" content="Viscacha(http: // www.viscacha.org)" />"},
			{"text": "<link rel="copyright" href="http: // www.viscacha.org" />", "certainty": "75 },
			{ "version" : "/Powered by <strong><a[^>]+href="http:\/\/www\.viscacha\.org" target="_blank">Viscacha ([^<]+)<\/a>/" },
		]
	return(self.rules)
