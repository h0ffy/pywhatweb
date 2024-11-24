import plugins


class Pluginclaroline_plugin(plugins.Base):
    def __init__(self):
    	pass

    def start(self):
        self.rules = [
			{"string": / <div id = "poweredBy" > [ ^ <]{1, 20} < a href = "http:\/\/www\.claroline\.net" target = "_blank" > Claroline <\/a> &copy; 2001 - (20[\d]{2})<\/div>/" },
			{ "certainty" : "75", "text" : "<link href="http://www.claroline.net/documentation.htm" rel="Help" />" },
			{ "certainty" : "75", "text" : "<link href="http://www.claroline.net/credits.htm" rel="Author" />" },
			{ "certainty" : "75", "text" : "<link href="http://www.claroline.net" rel="Copyright" />" },
		]
	return(self.rules)
