import plugins


class Pluginslaed_cms_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/<meta name="generator" content="SLAED CMS ([ ^ "^>]+)" > /" },
			{ "string" : /<br \/>Powered by <a href="http:\/\/www\.slaed\.net" target="_blank" title="SLAED CMS">SLAED CMS<\/a> &copy; 2005-(20[\d]{2}) SLAED/" },
		]
	return(self.rules)
