import plugins


class Pluginclansphere_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"text": "<title>ClanSphere - News</title>"},
			{"text": "<meta name="generator" content="ClanSphere" />"},
			{"regexp": "/Powered by <a href="http: \/\/www.csphere.eu[^>]+>Clansphere[\ CSP]*/i },
			{ "regexp" : "/<a href="[\/]*index.php\?mod=clansphere&amp;action=about[^>]+>Powered by Clansphere[\ CSP]*/i },
			{ "regexp" : "/<a href="[\/]*index.php\?mod=clansphere&amp;action=about[^>]+>Clansphere[\ CSP]*/i },
			{ "regexp" : "/powered by <a href="http:\/\/www.clansphere.net[^>]+>ClanSphere Project<\/a>/" },
		]
	return(self.rules)
