import plugins


class Pluginpiwik_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"certainty": "75", "ghdb": "+intitle:Piwik "JavaScript must be enabled in order for you to use Piwik in standard view""},
			{"text": "<title>Piwik &rsaquo; Web Analytics Reports</title>"},
			{"text": "<img src="themes / default / images / loading - blue.gif" alt=" / > Loading data" },
			{ "version" : "/<meta name=\"generator\"[^>]*content=\"Piwik ([0-9\.]+)/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^_pk_/", "name" : "_pk_ cookie" },
			{ "search" : "headers[set-cookie]", "regexp" : "/^PIWIK_SESSID/", "name" : "PIWIK_SESSID cookie" },
		]
	return(self.rules)
