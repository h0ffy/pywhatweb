import plugins


class Pluginredmine_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"search": "headers[set-cookie]", "regexp": "/_redmine_session=/"},
			{"string": / Powered by < a href = "http:\\/\\/www\\.redmine\\.org\\/" > Redmine <\/a> &copy; 2006-(20[\d]{2}) Jean-Philippe Lang/" },
			{ "certainty" : "25", "text" : "<meta name="description" content="Redmine" />" },
			{ "status" : "404", "text" : "<title>redMine 404 error</title>" },
		]
	return(self.rules)
