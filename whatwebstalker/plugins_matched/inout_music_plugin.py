import plugins
			
class Plugininout_music_plugin(plugins.Base):
    def __init__(self):
    	pass
    def start(self):
        self.rules = [
			{ "text" : "function trim(stringValue){return stringValue.replace(/(^\s*|\s*$)/", "");}", "certainty" : "75 },
			{ "text" : " href="http://www.inoutscripts.com/?r=13">Powered by Inoutscripts</a>" },
		]
		return(self.rules)
