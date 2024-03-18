import plugins
			
class Pluginphpbb_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "<!-- link rel="stylesheet" href="templates/subSilver/subSilver.css'},
			{ "text" : "/images/logo_phpBB.gif", "certainty" : "75},
			{ "text" : "We request you retain the full copyright notice below including the link to www.phpbb.com.'},
			{ "search" : "headers[set-cookie]", "version" : "/phpbb([\d])mysql_(data=a%3A|sid=[a-f\d]{32};)/" },
		]
		return(self.rules)

