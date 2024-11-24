import plugins


class Pluginuportal_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"ghdb": "powered by uportal"", "certainty" : "75},
			{"version": "/<img[^>]*alt="Powered by uPortal([\d\.]+)"[^>]*>/" },
			{ "version" : "/<a target="_blank" title="Powered by \$" href="http:\/\/www.uportal.org">Powered by uPortal ([^<]+)<\/a>/" },
		]
	return(self.rules)
