import plugins
			
class Pluginlightneasy_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "version" : "/<meta name='generator' content='LightNEasy( Mini)? ([^'^>]+)' \/>/", "offset" : "1 },
			{ "version" : "/<!-- \+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+[\s]+\| LightNEasy ([^\s]+) Content Management System[\s]+\| /" },
			{ "version" : "/<!-- \+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+[\s]+\| LightNEasy Content Management System[\s]+\| Copyright 2007-20[\d]{2} Fernando Baptista[\s]+\| http:\/\/(www\.)?lightneasy\.org[\s]+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+[\s]+\| [^\|]+ version ([^\s]+)/", "offset" : "1 },
			{ "string" : /<!-- \+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+[\s]+\| LightNEasy [^\s^\|]* Content Management System[\s]+\| ([^\|]+) version[\s]+/" },
			{ "string" : /<!-- \+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+[\s]+\| LightNEasy [^\s^\|]* Content Management System[\s]+\| Copyright 2007-20[\d]{2} Fernando Baptista[\s]+\| http:\/\/(www\.)?lightneasy\.org[\s]+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+\+[\s]+\| ([^\|]+) version [^\s]+/", "offset" : "1 },
			{ "text" : "<link rel='stylesheet' type='text/css' href='css/lightneasy.css' />" },
			{ "version" : "/Powered by <a href="http:\/\/lightneasy\.org">LightNEasy ([^<]+)<\/a>/" },
			{ "version" : "/<h1>LightNEasy ([^<^\s]+) index page<\/h1><p>If you are seeing this", "that means <strong>LightNEasy<\/strong> installation worked!<\/p>/" },
			{ "version" : "/<h2 class="LNE_title">LightNEasy ([^<^\s]+) index page<\/h2><p>If you are seeing this", "that means <strong>LightNEasy<\/strong> installation worked!<\/p>/" },
		]
		return(self.rules)

