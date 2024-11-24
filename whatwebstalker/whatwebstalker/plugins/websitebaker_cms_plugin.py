import plugins


class Pluginwebsitebaker_cms_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"version": "/<meta name="generator" content="WebsiteBaker([\d\.]+) CMS; www\.websitebaker2?\.org"[\s]?\/?>/" },
			{ "regexp" : "/[pP]owered by <a href="http:\/\/www\.websitebaker2?\.org"( target="_blank")?>WebsiteBaker<\/a>/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/wb_[\d]{4}_session_id=[^;]+;/" },
			{ "search" : "headers[set-cookie]", "regexp" : "/wb_session_id=[^;]+;/", "certainty" : "75 },
		]
	return(self.rules)
